import unittest
import random
from solver import k_largest

class TestSolver(unittest.TestCase):
  def test_k_largest(self):
    self.assertEqual(k_largest([3, 5, 2, 4, 6, 8], k=3), 5)
    self.assertEqual(k_largest([3, 5, 2, 4, 6, 8], k=1), 8)
    self.assertEqual(k_largest([3               ], k=1), 3)

if __name__ == "__main__":
    unittest.main()
