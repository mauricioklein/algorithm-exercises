import unittest
from solver import spiral_traverse

class TestSolver(unittest.TestCase):
  def test_spiral_traverse(self):
    arr =      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    rows, columns = 4, 4

    self.assertEqual(spiral_traverse(arr, rows, columns), expected)

if __name__ == "__main__":
    unittest.main()
