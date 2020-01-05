import unittest
from solver import has_palindrome

class TestSolver(unittest.TestCase):
  def test_has_palindrome(self):
    self.assertTrue (has_palindrome("waterrfetawx", 2))
    self.assertTrue (has_palindrome("waterrfetawx", 3))
    self.assertFalse(has_palindrome("waterrfetawx", 1))
    self.assertTrue (has_palindrome("waterretaw"  , 0))
    self.assertTrue (has_palindrome("yyyyaxxxx"   , 8))
    self.assertTrue (has_palindrome("yyyyxxxx"    , 8))

if __name__ == "__main__":
    unittest.main()
