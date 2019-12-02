import unittest
from solver import closest_coin

class TestSolver(unittest.TestCase):
  def test_closest_coin(self):
    self.assertEqual(closest_coin([(0,4), (1,0), (2,0), (3,2)], (0,2)), (0,4))
    self.assertEqual(closest_coin([(0,0), (0,4)              ], (0,2)), (0,0))
    self.assertEqual(closest_coin([                          ], (0,2)), None )

if __name__ == "__main__":
    unittest.main()
