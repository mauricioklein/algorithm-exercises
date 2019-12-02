import unittest
from solver import buddy_strings

class TestSolver(unittest.TestCase):
  def test_buddy_strings(self):
    self.assertEqual(buddy_strings("ab"       , "ba"       ), True )
    self.assertEqual(buddy_strings("ab"       , "ab"       ), False)
    self.assertEqual(buddy_strings("aa"       , "aa"       ), True )
    self.assertEqual(buddy_strings("aaaaaaabc", "aaaaaaacb"), True )
    self.assertEqual(buddy_strings(""         , "aa"       ), False)

if __name__ == "__main__":
    unittest.main()
