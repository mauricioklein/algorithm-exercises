import unittest
from solver import find_ranges

class TestSolver(unittest.TestCase):
  def test_find_ranges(self):
    test_cases = [
      [
        [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15],
        ['0->2', '5->5', '7->11', '15->15']
      ],
      [
        [0, 1, 2, 3, 4, 5],
        ['0->5']
      ],
      [
        [0, 2, 4, 6],
        ['0->0', '2->2', '4->4', '6->6']
      ],
      [
        [2, 2, 2, 2, 2],
        ['2->2']
      ],
      [
        [],
        []
      ]
    ]

    for nums, expected_output in test_cases:
      self.assertEqual(find_ranges(nums), expected_output)

if __name__ == "__main__":
    unittest.main()
