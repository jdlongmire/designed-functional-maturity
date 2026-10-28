"""Strict, non-fitting admission audit for independently sourced U-Pb analyses.

This module never imputes absent uncertainties or common-Pb corrections.
"""
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

FIELDS = ('source_doi','source_sha256','analysis_id','rock_unit','laboratory','method',
          'r68','r75','sigma68_abs_1s','sigma75_abs_1s','rho_wetherill',
          'common_pb_method','correction_status','measurement_basis')

def audit(path, *, expected_sha256=None):
    path = Path(path)
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if expected_sha256 and digest != expected_sha256:
        raise ValueError('Source checksum mismatch')
    with path.open(newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        missing = sorted(set(FIELDS) - set(reader.fieldnames or []))
        if missing:
            raise ValueError('Missing columns: ' + ', '.join(missing))
        rows = list(reader)
    accepted, rejected, seen = [], [], set()
    for line, row in enumerate(rows, 2):
        reasons = []
        for field in ('source_doi','source_sha256','analysis_id','rock_unit','laboratory',
                      'method','common_pb_method','correction_status','measurement_basis'):
            if not (row.get(field) or '').strip():
                reasons.append('missing_' + field)
        if row.get('source_sha256') and row['source_sha256'].strip().lower() == digest:
            # A source file cannot reliably embed its own SHA-256: require the SHA of
            # original raw source bytes, not this normalized admission table.
            reasons.append('source_hash_must_reference_original_raw_data')
        if row.get('analysis_id') in seen:
            reasons.append('duplicate_analysis_id')
        seen.add(row.get('analysis_id'))
        vals = {}
        for field in ('r68','r75','sigma68_abs_1s','sigma75_abs_1s','rho_wetherill'):
            try:
                vals[field] = float(row[field])
                if not math.isfinite(vals[field]): raise ValueError()
            except (ValueError, TypeError, KeyError):
                reasons.append('invalid_' + field)
        if len(vals) == 5:
            if vals['r68'] < 0 or vals['r75'] < 0: reasons.append('negative_ratio')
            if vals['sigma68_abs_1s'] <= 0 or vals['sigma75_abs_1s'] <= 0:
                reasons.append('nonpositive_uncertainty')
            if not -1 < vals['rho_wetherill'] < 1:
                reasons.append('non_positive_definite_covariance')
        if row.get('correction_status') != 'corrected_radiogenic':
            reasons.append('not_confirmed_radiogenic_ratios')
        if row.get('measurement_basis') != 'wetherill_absolute_1sigma':
            reasons.append('unverified_uncertainty_or_ratio_basis')
        if reasons:
            rejected.append({'line':line,'analysis_id':row.get('analysis_id'),'reasons':sorted(set(reasons))})
        else:
            accepted.append(row)
    return {'admission_table_sha256':digest,'total':len(rows),'accepted':len(accepted),
            'rejected':len(rejected),'rejection_reasons':dict(Counter(r for x in rejected for r in x['reasons'])),
            'rejections':rejected,'accepted_ids':[x['analysis_id'] for x in accepted],
            'status':'AUDITED_NOT_FROZEN'}

if __name__ == '__main__':
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument('normalized_csv')
    p.add_argument('--expected-sha256')
    args=p.parse_args()
    print(json.dumps(audit(args.normalized_csv,expected_sha256=args.expected_sha256),indent=2))
