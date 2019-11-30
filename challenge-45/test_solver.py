import unittest
from solver import occurrences

class TestSolver(unittest.TestCase):
  def test_occurrences(self):
    self.assertEqual(occurrences([1, 2, 2, 2, 5, 7, 9], k=2), 3)
    self.assertEqual(occurrences([1, 2, 5, 7, 8, 9, 9], k=9), 2)
    self.assertEqual(occurrences([1, 1, 2, 5, 7, 8, 9], k=1), 2)
    self.assertEqual(occurrences([1, 2, 3, 5, 7, 8, 9], k=0), 0)

if __name__ == "__main__":
    unittest.main()
