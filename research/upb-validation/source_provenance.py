"""Verify original observation bytes against an explicit provenance manifest.

No network retrieval, inference of isotope fields, or silent checksum repair.
"""
import argparse
import hashlib
import json
from pathlib import Path

REQUIRED = ('doi', 'source_url', 'filename', 'sha256', 'retrieved_utc', 'license', 'source_type')

def verify(manifest_path, raw_dir):
    manifest = json.loads(Path(manifest_path).read_text(encoding='utf-8'))
    if not isinstance(manifest, list) or not manifest:
        raise ValueError('Manifest must be a nonempty list')
    raw_dir = Path(raw_dir).resolve()
    results = []
    seen = set()
    for i, entry in enumerate(manifest):
        missing = [k for k in REQUIRED if not isinstance(entry.get(k), str) or not entry[k].strip()]
        if missing:
            raise ValueError(f'Entry {i} missing: {missing}')
        filename = entry['filename']
        if Path(filename).name != filename or filename in ('.', '..'):
            raise ValueError(f'Unsafe filename: {filename}')
        if filename in seen:
            raise ValueError(f'Duplicate filename: {filename}')
        seen.add(filename)
        expected = entry['sha256'].lower()
        if len(expected) != 64 or any(c not in '0123456789abcdef' for c in expected):
            raise ValueError(f'Invalid sha256 for {filename}')
        path = raw_dir / filename
        if not path.is_file():
            results.append({'filename': filename, 'status': 'MISSING'}); continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        results.append({'filename': filename, 'status': 'VERIFIED' if actual == expected else 'HASH_MISMATCH', 'sha256': actual})
    return {'status': 'VERIFIED' if all(x['status'] == 'VERIFIED' for x in results) else 'BLOCKED', 'sources': results}

if __name__ == '__main__':
    p = argparse.ArgumentParser();p.add_argument('manifest_json');p.add_argument('raw_dir')
    a = p.parse_args(); print(json.dumps(verify(a.manifest_json, a.raw_dir), indent=2))
