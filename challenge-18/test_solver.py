import unittest
from solver import Solution

class TestSolver(unittest.TestCase):
    def test_solver(self):
        self.assertEqual(Solution().longestPalindrome("banana"), "anana")
        self.assertEqual(Solution().longestPalindrome("million"), "illi")
        self.assertEqual(Solution().longestPalindrome("arara"), "arara")
        self.assertEqual(Solution().longestPalindrome("abcxyz"), "a")
        self.assertEqual(Solution().longestPalindrome(""), "")

if __name__ == "__main__":
    unittest.main()
