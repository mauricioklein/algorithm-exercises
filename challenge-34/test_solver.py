import unittest
from solver import subset_sum

class TestSolver(unittest.TestCase):
  def test_queen(self):
    self.assertTrue (subset_sum((3, 34, 4, 12, 5, 2), 8)) # True: (3,5)
    self.assertFalse(subset_sum((3, 34, 4, 12, 5, 2), 1)) # False
    self.assertTrue (subset_sum((1,  1, 1,  1, 1   ), 5)) # True: (1,1,1,1,1)
    self.assertFalse(subset_sum((1,  1, 1,  1, 1   ), 6)) # False
    self.assertTrue (subset_sum((                  ), 0)) # True: ()

if __name__ == "__main__":
    unittest.main()
