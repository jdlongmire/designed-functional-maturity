import importlib.util
import tempfile
import unittest
from pathlib import Path

P = Path(__file__).resolve().parents[1] / 'research/upb-validation/acquisition_inventory.py'
spec = importlib.util.spec_from_file_location('acquisition_inventory', P)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class AcquisitionInventoryTests(unittest.TestCase):
    def test_empty_dir_is_incomplete(self):
        with tempfile.TemporaryDirectory() as d:
            result = m.inventory(d)
            self.assertEqual(result['status'], 'INCOMPLETE')
            self.assertEqual(len(result['files']), 3)
    def test_partial_dir_is_incomplete(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / m.RELEASES['manzano']['files'][0]).write_bytes(b'not actual measurements')
            result = m.inventory(d)
            self.assertEqual(result['status'], 'INCOMPLETE')
            self.assertEqual(result['files'][0]['status'], 'PRESENT_UNVERIFIED')
    def test_full_dir_still_not_admitted(self):
        with tempfile.TemporaryDirectory() as d:
            for name in m.RELEASES['manzano']['files']:
                (Path(d) / name).write_bytes(b'fixture')
            result = m.inventory(d)
            self.assertEqual(result['status'], 'AWAITING_PROVENANCE')
            self.assertTrue(all(f['status'] == 'PRESENT_UNVERIFIED' for f in result['files']))
    def test_unknown_release_rejected(self):
        with self.assertRaises(ValueError):
            m.inventory('.', 'unverified')
