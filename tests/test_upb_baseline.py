"""Dependency-free checks for the synthetic U-Pb reference model."""
import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'research' / 'upb-validation'))
import upb_baseline as model

class UPbBaselineTests(unittest.TestCase):
    def test_zero_time(self):
        self.assertEqual(model.conventional(0), (0.0, 0.0))
    def test_zero_initial_inventory(self):
        for ma in (0, 1, 10, 100, 500, 1000, 2500, 4500):
            self.assertEqual(model.initialized(ma*1e6, 0, 0), model.conventional(ma*1e6))
    def test_inverse_roundtrip(self):
        for ma in (0, 1, 10, 100, 500, 1000, 2500, 4500):
            a, b = model.conventional(ma*1e6)
            x, y = model.conventional_inverse(a, b)
            self.assertAlmostEqual(x/1e6, ma, places=7)
            self.assertAlmostEqual(y/1e6, ma, places=7)
    def test_nonnegative_and_monotone(self):
        ages = (0, 1e6, 1e8, 1e9, 4.5e9)
        vals = [model.conventional(t) for t in ages]
        for index in (0, 1):
            self.assertTrue(all(v[index] >= 0 for v in vals))
            self.assertTrue(all(vals[i][index] < vals[i+1][index] for i in range(len(vals)-1)))
    def test_negative_inverse_rejected(self):
        for pair in ((-0.01, 0.1), (0.1, -0.01)):
            with self.assertRaises(ValueError):
                model.conventional_inverse(*pair)
    def test_nonzero_initial_inventory(self):
        t=1e9
        a,b=model.initialized(t,0.05,0.1)
        c,d=model.conventional(t)
        self.assertAlmostEqual(a-c,0.05*math.exp(model.L238*t))
        self.assertAlmostEqual(b-d,0.1*math.exp(model.L235*t))

if __name__ == '__main__':
    unittest.main()
