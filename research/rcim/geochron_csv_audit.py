"""Read-only schema/coverage audit of an official Geochron CSV export.

Usage: python research/rcim/geochron_csv_audit.py path/to/export.csv
Outputs field presence and nonempty counts. Never selects/fits an isotope model.
"""
import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

FIELD_GROUPS = {
    "u_pb_ratio": ("pb206u238", "pb207u235"),
    "u_pb_sigma_1": ("pb206u238unc1s", "pb207u235unc1s"),
    "u_pb_sigma_2": ("pb206u238unc2s", "pb207u235unc2s"),
    "u_pb_correlation": ("rhowetherill",),
    "th_pb": ("pb208th232", "pb208th232unc"),
    "common_pb_correction": ("pb204corrpb206u238",),
    "analysis_id": ("analysis_id",),
}
def audit(path):
    path = Path(path)
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(block)
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise ValueError("Missing CSV header")
        headers = reader.fieldnames
        if len(headers) != len(set(headers)):
            raise ValueError("Duplicate CSV column names")
        normalized = {h.casefold(): h for h in headers}
        wanted = sorted({name for fields in FIELD_GROUPS.values() for name in fields})
        present = {name: normalized.get(name.casefold()) for name in wanted}
        nonempty = Counter()
        count = 0
        for row in reader:
            count += 1
            for name, actual in present.items():
                if actual and row.get(actual, "").strip():
                    nonempty[name] += 1
    return {
        "source_file": str(path),
        "sha256": digest.hexdigest(),
        "row_count": count,
        "field_audit": {group: {
            name: {"present": present[name] is not None, "nonempty": nonempty[name]}
            for name in fields
        } for group, fields in FIELD_GROUPS.items()},
        "notes": ["Schema presence does not establish suitability, covariance completeness, or data provenance.",
                  "No sample selection, fitting, or experimental freeze performed."]
    }
def self_test():
    import tempfile
    with tempfile.TemporaryDirectory() as folder:
        p = Path(folder) / "test.csv"
        p.write_text("analysis_id,pb206u238,pb207u235,rhowetherill\nA,0.1,0.2,0.5\nB,0.2,,\n", encoding="utf-8")
        result = audit(p)
        assert result["row_count"] == 2
        assert result["field_audit"]["u_pb_ratio"]["pb206u238"]["nonempty"] == 2
        assert result["field_audit"]["u_pb_ratio"]["pb207u235"]["nonempty"] == 1
        assert not result["field_audit"]["th_pb"]["pb208th232"]["present"]
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", nargs="?")
    args = parser.parse_args()
    if args.csv_path:
        print(json.dumps(audit(args.csv_path), indent=2))
    else:
        self_test()
        print("Geochron CSV audit self-test passed; no external data loaded")
