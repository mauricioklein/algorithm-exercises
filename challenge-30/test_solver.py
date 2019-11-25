import unittest
from solver import merge_sort

class TestSolver(unittest.TestCase):
  def test_merge_sort(self):
    self.assertEqual(merge_sort([5, 2, 3, 1, 4]), [ 1, 2, 3, 4, 5])
    self.assertEqual(merge_sort([4, 2, 3, 1, 4]), [ 1, 2, 3, 4, 4])
    self.assertEqual(merge_sort([4, 2, 3, 1,-5]), [-5, 1, 2, 3, 4])
    self.assertEqual(merge_sort([             ]), [              ])

if __name__ == "__main__":
    unittest.main()
