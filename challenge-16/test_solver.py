import unittest
from solver import Solution

class TestSolver(unittest.TestCase):
    def test_solver(self):
        self.assertEqual(Solution().addTwoNumbers([2,4,3  ], [5,6,4  ]), [7,0,8  ])
        self.assertEqual(Solution().addTwoNumbers([2,4,3,1], [5,6,4  ]), [7,0,8,1])
        self.assertEqual(Solution().addTwoNumbers([2,4,3  ], [5,6,4,1]), [7,0,8,1])
        self.assertEqual(Solution().addTwoNumbers([1,2,3  ], [       ]), [1,2,3  ])
        self.assertEqual(Solution().addTwoNumbers([       ], [1,2,3  ]), [1,2,3  ])
        self.assertEqual(Solution().addTwoNumbers([       ], [       ]), [       ])

if __name__ == "__main__":
    unittest.main()
