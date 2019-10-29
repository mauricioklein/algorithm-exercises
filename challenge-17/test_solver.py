import unittest
from solver import Solution

class TestSolver(unittest.TestCase):
    def test_solver(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxx"), 10)
        self.assertEqual(Solution().lengthOfLongestSubstring("abcdefghij"), 10)
        self.assertEqual(Solution().lengthOfLongestSubstring("aaaaaaaaaa"), 1)
        self.assertEqual(Solution().lengthOfLongestSubstring(""), 0)

if __name__ == "__main__":
    unittest.main()
