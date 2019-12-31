import unittest
from solver import group_anagrams

class TestSolver(unittest.TestCase):
  def test_group_anagrams(self):
    anagrams = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
    expected_groups = [['eat', 'ate', 'tea'],
                       ['apt', 'pat'],
                       ['now']]
    self.assertItemsEqual(group_anagrams(anagrams), expected_groups)

if __name__ == "__main__":
    unittest.main()
