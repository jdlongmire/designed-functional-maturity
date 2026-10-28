import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

PATH=Path(__file__).resolve().parents[1]/'research/upb-validation/audit_cohort.py'
spec=importlib.util.spec_from_file_location('audit_cohort',PATH)
audit_module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit_module)

class AdmissionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path=Path(self.tmp.name)/'admission.csv'
        self.row=dict.fromkeys(audit_module.FIELDS,'x')
        self.row.update(source_sha256='a'*64,analysis_id='grain-1',r68='0.1',r75='1.2',
                        sigma68_abs_1s='0.001',sigma75_abs_1s='0.01',rho_wetherill='0.4',
                        correction_status='corrected_radiogenic',measurement_basis='wetherill_absolute_1sigma')
    def write(self,rows,fields=None):
        with self.path.open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields or audit_module.FIELDS)
            w.writeheader();w.writerows(rows)
    def test_valid_row(self):
        self.write([self.row]);self.assertEqual(audit_module.audit(self.path)['accepted'],1)
    def test_invalid_covariance(self):
        self.row['rho_wetherill']='1';self.write([self.row])
        self.assertIn('non_positive_definite_covariance',audit_module.audit(self.path)['rejections'][0]['reasons'])
    def test_missing_correction(self):
        self.row['correction_status']='uncorrected';self.write([self.row])
        self.assertEqual(audit_module.audit(self.path)['accepted'],0)
    def test_duplicate(self):
        self.write([self.row,self.row]);self.assertEqual(audit_module.audit(self.path)['accepted'],1)
    def test_checksum_guard(self):
        self.write([self.row]);self.assertRaises(ValueError,audit_module.audit,self.path,expected_sha256='0'*64)
    def test_missing_column(self):
        fields=list(audit_module.FIELDS);fields.remove('rho_wetherill')
        row={k:v for k,v in self.row.items() if k in fields};self.write([row],fields)
        self.assertRaises(ValueError,audit_module.audit,self.path)
    def test_nan(self):
        self.row['r68']='NaN';self.write([self.row]);self.assertEqual(audit_module.audit(self.path)['accepted'],0)

if __name__=='__main__':unittest.main()
