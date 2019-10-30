import unittest
from solver import Solution

class TestSolver(unittest.TestCase):
    def test_solver(self):
        klass = Solution()

        self.assertEqual(klass.getRange([1,3,3,5,7,8,9,9,15     ], target=9  ), [  6,  7])
        self.assertEqual(klass.getRange([1,3,3,5,7,8,9,9,15     ], target=7  ), [  4,  4])
        self.assertEqual(klass.getRange([100,150,150,153        ], target=150), [  1,  2])
        self.assertEqual(klass.getRange([100,100,100,150,150,200], target=100), [  0,  2])
        self.assertEqual(klass.getRange([100,150,200,200,200    ], target=200), [  2,  4])
        self.assertEqual(klass.getRange([1,2,3,4,5,6,10         ], target=9  ), [- 1, -1])
        self.assertEqual(klass.getRange( range(1000000)         , target=500), [500,500])

if __name__ == "__main__":
    unittest.main()
