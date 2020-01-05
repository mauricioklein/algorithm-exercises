import unittest
from solver import jumps_to_end

class TestSolver(unittest.TestCase):
  def test_jumps_to_end(self):
    self.assertEqual(jumps_to_end([3, 2, 5, 1, 1, 9, 3, 4]), 2) # (3 -> 5 -> 4)
    self.assertEqual(jumps_to_end([1, 1, 1, 1, 1]         ), 4) # (1 -> 1 -> 1 -> 1 -> 1)
    self.assertEqual(jumps_to_end([2, 2, 0, 1, 1]         ), 3) # (2 -> 2 -> 1 -> 1)
    self.assertEqual(jumps_to_end([2]                     ), 0) # (2)

    self.assertEqual(jumps_to_end([2, 0, 0, 1, 1]), float('inf')) # (No solution possible)

if __name__ == "__main__":
    unittest.main()
