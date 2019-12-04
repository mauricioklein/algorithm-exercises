import unittest
from solver import Node, deepest

class TestSolver(unittest.TestCase):
  def test_deepest(self):
    a, b, c, d = Node('a'), Node('b'), Node('c'), Node('d')

    root = a
    root.left = b
    b.left = d
    root.right = c

    self.assertEqual(deepest(root), (d, 3))

if __name__ == "__main__":
    unittest.main()
