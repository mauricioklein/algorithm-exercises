import unittest
from solver import Solution

class TestSolver(unittest.TestCase):
  def test_move_zeros(self):
    self.assertEqual(Solution().move_zeros([ 1,  0, 3,  5, 0, 12]), [ 1,  3,  5, 12, 0,  0])
    self.assertEqual(Solution().move_zeros([ 3,  0, 1, 12, 0,  5]), [ 3,  1, 12,  5, 0,  0])
    self.assertEqual(Solution().move_zeros([ 1, 20, 3,  5, 8, 12]), [ 1, 20,  3,  5, 8, 12])
    self.assertEqual(Solution().move_zeros([-1,  0, 2, -3, 0,  0]), [-1,  2, -3,  0, 0,  0])
    self.assertEqual(Solution().move_zeros([ 0,  0, 0,  0       ]), [ 0,  0,  0,  0       ])
    self.assertEqual(Solution().move_zeros([                    ]), [                     ])

if __name__ == "__main__":
    unittest.main()
