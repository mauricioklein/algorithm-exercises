import unittest
import solver
from solver import sort_colors

class TestSolver(unittest.TestCase):
  def test_sort_colors(self):
    self.assertEqual(sort_colors([0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0])
    self.assertEqual(sort_colors([2, 2, 2, 2, 2, 2]), [2, 2, 2, 2, 2, 2])
    self.assertEqual(sort_colors([0, 0, 2, 0, 0, 0]), [0, 0, 0, 0, 0, 2])
    self.assertEqual(sort_colors([0, 0, 0, 0, 1, 0]), [0, 0, 0, 0, 0, 1])
    self.assertEqual(sort_colors([2, 2, 1, 2, 2, 2]), [1, 2, 2, 2, 2, 2])
    self.assertEqual(sort_colors([0, 2, 2, 0, 2, 0]), [0, 0, 0, 2, 2, 2])
    self.assertEqual(sort_colors([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])

if __name__ == "__main__":
    unittest.main()
