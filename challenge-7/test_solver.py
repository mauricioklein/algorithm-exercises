import unittest
from solver import Solution

class TestSolver(unittest.TestCase):
  def test_solver(self):
    self.assertEqual(Solution().first_missing_positive([3, 4, -1, 1]), 2)
    self.assertEqual(Solution().first_missing_positive([1, 2, 0])    , 3)
    self.assertEqual(Solution().first_missing_positive([2, 1, 3])    , 4)
    self.assertEqual(Solution().first_missing_positive([])           , 1)

if __name__ == "__main__":
    unittest.main()
