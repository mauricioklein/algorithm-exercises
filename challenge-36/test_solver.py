import unittest
from solver import buy_and_sell

class TestSolver(unittest.TestCase):
  def test_buy_and_sell(self):
    self.assertEqual(buy_and_sell((9, 11, 8, 5, 7, 10)), 5) # Buy on "5" and sell on "10"
    self.assertEqual(buy_and_sell((9, 11, 5, 2, 6, 6 )), 4) # Buy on "2" and sell on "6"
    self.assertEqual(buy_and_sell((4, 4, 4, 4        )), 0) # Buy and sell for the same price
    self.assertEqual(buy_and_sell((4, 3, 2, 1        )), 0) # Lost money: profit zero
    self.assertEqual(buy_and_sell((                  )), 0)

if __name__ == "__main__":
    unittest.main()
