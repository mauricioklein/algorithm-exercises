import unittest
from solver import tree_depth

class TestSolver(unittest.TestCase):
  def test_tree_depth(self):
    self.assertEqual(tree_depth("(00)"         ), 1)
    self.assertEqual(tree_depth("((00)(00))"   ), 2)
    self.assertEqual(tree_depth("((0(00))(00))"), 3)

if __name__ == "__main__":
    unittest.main()
