import unittest, random
from solver import first_thousand_missing

class TestSolver(unittest.TestCase):
  def test_first_thousand_missing(self):
    nums = range(1,1000001)
    missing = random.sample(nums, 1000)

    # Remove the missing values from the array
    for num in missing:
      nums.remove(num)

    # Shuffle the array
    random.shuffle(nums)

    # Sort the missing values
    missing.sort()

    self.assertEqual(first_thousand_missing(nums), missing)

if __name__ == "__main__":
    unittest.main()
