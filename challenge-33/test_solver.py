import unittest
from solver import merge_overlapping_intervals

class TestSolver(unittest.TestCase):
  def test_partial_overlapping(self):
    self.assertEqual(merge_overlapping_intervals([(1, 3), (5, 8) , (4, 10), (20, 25)]), [(1, 3), (4, 10), (20, 25)])

  def test_full_overlap(self):
    self.assertEqual(merge_overlapping_intervals([(1, 3), (5, 8) , (6, 7), (20, 25)]), [(1, 3), (5, 8), (20, 25)])

  def test_multiple_overlaps(self):
    self.assertEqual(merge_overlapping_intervals([(1, 5), (3, 6) , (4, 9), (20, 25)]), [(1, 9), (20, 25)])

  def test_no_overlaps(self):
    self.assertEqual(merge_overlapping_intervals([(1, 4), (5, 8), (20, 25)]), [(1, 4), (5, 8), (20, 25)])

  def test_no_intervals(self):
    self.assertEqual(merge_overlapping_intervals([]), [])

if __name__ == "__main__":
    unittest.main()
