import unittest
from solver import remove_exponential, remove_linear

class TestSolver(unittest.TestCase):
  def test_remove_exponential(self):
    nums = [10, 5, -3, -3, 1, 4, -4]
    expected = [10]
    self.assertEqual(remove_exponential(nums), expected)

    nums = [10, 5, 2, -2, -5, -10]
    expected = []
    self.assertEqual(remove_exponential(nums), expected)

  def test_remove_linear(self):
    nums = [10, 5, -3, -3, 1, 4, -4]
    expected = [10]
    self.assertEqual(remove_linear(nums), expected)

    nums = [10, 5, 2, -2, -5, -10]
    expected = []
    self.assertEqual(remove_linear(nums), expected)

if __name__ == "__main__":
    unittest.main()
