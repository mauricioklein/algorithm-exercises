import unittest
from solver import look_and_say

class TestSolver(unittest.TestCase):
  def test_look_and_say(self):
    self.assertEqual(look_and_say(1), "1")
    self.assertEqual(look_and_say(2), "11")
    self.assertEqual(look_and_say(3), "21")
    self.assertEqual(look_and_say(4), "1211")
    self.assertEqual(look_and_say(5), "111221")

if __name__ == "__main__":
    unittest.main()
