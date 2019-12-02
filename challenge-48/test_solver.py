import unittest
from solver import subarr_mean 

class TestSolver(unittest.TestCase):
  def test_closest_coin(self):
    self.assertEqual(subarr_mean([-1, 5, 13, 8, 2, 3, 3, 1], k=3), [5, 8, 8, 3, 3, 3])
    self.assertEqual(subarr_mean([-1, 5, 13, 8, 2, 3, 3, 1], k=4), [6, 6, 5, 3, 2   ])
    self.assertEqual(subarr_mean([1, 2, 3, 4              ], k=1), [1, 2, 3, 4      ])
    self.assertEqual(subarr_mean([1, 50, 10, 20           ], k=4), [15              ])

if __name__ == "__main__":
    unittest.main()
