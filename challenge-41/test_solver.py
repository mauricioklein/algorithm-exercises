import unittest
import random
from solver import max_sequence_length

class TestSolver(unittest.TestCase):
  def test_max_sequence_length(self):
    nums = [1,2,3,4,5,99,100]
    random.shuffle(nums)
    self.assertEqual(max_sequence_length(nums), 5) # [1, 2, 3, 4, 5]

    nums = [1,2,5,6,7,15,16]
    random.shuffle(nums)
    self.assertEqual(max_sequence_length(nums), 3) # [5, 6, 7]

    nums = [1,3,5,7,9]
    random.shuffle(nums)
    self.assertEqual(max_sequence_length(nums), 1)

    nums = [-2,-1,0,1,2,5,6]
    random.shuffle(nums)
    self.assertEqual(max_sequence_length(nums), 5) # [-2, -1, 0, 1, 2]

    nums = [1,2,5,6,7,8,9]
    random.shuffle(nums)
    self.assertEqual(max_sequence_length(nums), 5) # [5,6,7,8,9]
    
    nums = []
    random.shuffle(nums)
    self.assertEqual(max_sequence_length(nums), 0)

if __name__ == "__main__":
    unittest.main()
