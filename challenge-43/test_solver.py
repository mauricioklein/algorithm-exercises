import unittest
from solver import max_subarray

class TestSolver(unittest.TestCase):
  def test_max_subarray(self):
    self.assertEqual(max_subarray([34, -50, 42, 14, -5, 86]), 137) # Max sum is given by "[42, 14, -5, 86]"
    self.assertEqual(max_subarray([-1, -2, -3             ]),   0) # Max sum is given by "[]"
    self.assertEqual(max_subarray([-1, 1, 1, 1, -1, 4, -1 ]),   6) # Max sum is given by "[1, 1, 1, -1, 4]"
    self.assertEqual(max_subarray([                       ]),   0) # Max sum is given by "[]"

if __name__ == "__main__":
    unittest.main()
