"""Inventory original USGS files without treating a partial download as admitted data."""
import argparse
import hashlib
import json
from pathlib import Path

RELEASES = {
    'manzano': {
        'doi': '10.5066/P9U0P2ZY',
        'files': (
            'geochronology_SHRIMP-RG_manzanoMtns_jones.csv',
            'geochronology_sampleSummary_manzanoMtns_jones.csv',
            'geochronology_dataDictionary_manzanoMtns_jones.csv',
        ),
    },
}

def inventory(raw_dir, release='manzano'):
    if release not in RELEASES:
        raise ValueError('Unknown release')
    root = Path(raw_dir).resolve()
    records = []
    for filename in RELEASES[release]['files']:
        path = root / filename
        if not path.is_file() or path.is_symlink():
            records.append({'filename': filename, 'status': 'MISSING'})
            continue
        raw = path.read_bytes()
        records.append({'filename': filename, 'status': 'PRESENT_UNVERIFIED',
                        'size_bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
    return {'release': release, 'doi': RELEASES[release]['doi'],
            'status': 'AWAITING_PROVENANCE' if all(x['status'] == 'PRESENT_UNVERIFIED' for x in records)
            else 'INCOMPLETE', 'files': records,
            'note': 'Hashes describe local bytes; they do not independently authenticate source provenance.'}

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('raw_dir')
    p.add_argument('--release', default='manzano', choices=sorted(RELEASES))
    args = p.parse_args()
    print(json.dumps(inventory(args.raw_dir, args.release), indent=2))
