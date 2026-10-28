import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'research/upb-validation/source_provenance.py'
s=importlib.util.spec_from_file_location('source_provenance',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.d=Path(self.tmp.name);(self.d/'raw.csv').write_bytes(b'one,two\n1,2\n')
        self.e={'doi':'10.5066/P9U0P2ZY','source_url':'https://doi.org/10.5066/P9U0P2ZY','filename':'raw.csv','sha256':hashlib.sha256((self.d/'raw.csv').read_bytes()).hexdigest(),'retrieved_utc':'2026-10-28T00:00:00Z','license':'CC0','source_type':'original'}
    def run_check(self):
        p=self.d/'manifest.json';p.write_text(json.dumps([self.e]));return m.verify(p,self.d)
    def test_valid(self):self.assertEqual(self.run_check()['status'],'VERIFIED')
    def test_modified_bytes(self):
        (self.d/'raw.csv').write_bytes(b'modified');self.assertEqual(self.run_check()['status'],'BLOCKED')
    def test_missing(self):
        (self.d/'raw.csv').unlink();self.assertEqual(self.run_check()['sources'][0]['status'],'MISSING')
    def test_traversal(self):
        self.e['filename']='../raw.csv';self.assertRaises(ValueError,self.run_check)
    def test_bad_hash(self):
        self.e['sha256']='invalid';self.assertRaises(ValueError,self.run_check)
    def test_missing_provenance(self):
        self.e['doi']='';self.assertRaises(ValueError,self.run_check)
if __name__=='__main__':unittest.main()
