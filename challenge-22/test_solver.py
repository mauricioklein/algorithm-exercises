import unittest
from solver import Solution

class TestSolver(unittest.TestCase):
  def test_solver(self):
    self.assertEqual(Solution().two_sum([4,7,1,-3,2],  5), True )
    self.assertEqual(Solution().two_sum([4,7,1,-3,2], 10), False)
    self.assertEqual(Solution().two_sum([2,2,2,2,2 ],  4), True )
    self.assertEqual(Solution().two_sum([2         ],  2), False)
    self.assertEqual(Solution().two_sum([2,4,0     ],  4), True )
    self.assertEqual(Solution().two_sum([2,4,6,-4  ],  0), True )
    self.assertEqual(Solution().two_sum([          ],  0), False)

if __name__ == "__main__":
    unittest.main()
