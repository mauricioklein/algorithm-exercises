import unittest
from solver import Solution

class TestSolver(unittest.TestCase):
  def test_solver_V1(self):
    self.assertEqual(Solution().sortNumsV1([3, 3, 2, 1, 3, 2, 1]), [1, 1, 2, 2, 3, 3, 3])


  def test_solver_V1(self):
    self.assertEqual(Solution().sortNumsV2([3, 3, 2, 1, 3, 2, 1]), [1, 1, 2, 2, 3, 3, 3])

if __name__ == "__main__":
    unittest.main()
