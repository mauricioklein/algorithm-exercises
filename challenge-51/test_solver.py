import unittest
from solver import subsequences

class TestSolver(unittest.TestCase):
  def test_subsequences(self):
    self.assertEqual(subsequences("xyz"), ['xyz', 'xy', 'xz', 'x', 'yz', 'y', 'z', ''])
    self.assertEqual(subsequences("aba"), ['aba', 'ab', 'aa', 'a', 'ba', 'b', 'a', ''])
    self.assertEqual(subsequences(""   ), [                                        ''])

if __name__ == "__main__":
    unittest.main()
