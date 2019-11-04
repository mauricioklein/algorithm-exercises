import unittest
from solver import Node, Solution

class TestSolver(unittest.TestCase):
  def test_invert_recursively(self):
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')

    self.assertEqual(root.string(), "abdecf")
    Solution().invert_recursively(root)
    self.assertEqual(root.string(), "acfbed")

  def test_invert_iteratively(self):
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')

    self.assertEqual(root.string(), "abdecf")
    Solution().invert_iteratively(root)
    self.assertEqual(root.string(), "acfbed")

if __name__ == "__main__":
    unittest.main()
