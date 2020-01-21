import unittest
from solver import Node, level_order

class TestSolver(unittest.TestCase):
  def test_level_order(self):
    root = Node(1, Node(2), Node(3, Node(4), Node(5)))
    self.assertEqual(level_order(root), [1, 2, 3, 4, 5])

    root = Node(1, right=Node(3, right=Node(5)))
    self.assertEqual(level_order(root), [1, 3, 5])

    root = Node(1, left=Node(2, left=Node(4)))
    self.assertEqual(level_order(root), [1, 2, 4])

    root = Node(1)
    self.assertEqual(level_order(root), [1])

    root = None
    self.assertEqual(level_order(root), [])

if __name__ == "__main__":
    unittest.main()
