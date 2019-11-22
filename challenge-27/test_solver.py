import unittest
from solver import witnesses

class TestSolver(unittest.TestCase):
  def test_witnesses(self):
    self.assertEqual(witnesses([3, 6, 3, 4, 1]), 3)
    self.assertEqual(witnesses([5, 4, 3, 2, 1]), 5)
    self.assertEqual(witnesses([1, 2, 3, 4, 5]), 1)
    self.assertEqual(witnesses([2, 2, 2, 2, 2]), 1)
    self.assertEqual(witnesses([5, 1, 2, 3, 4]), 2)
    self.assertEqual(witnesses([             ]), 0)

if __name__ == "__main__":
    unittest.main()
