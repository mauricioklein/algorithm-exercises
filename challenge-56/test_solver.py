import unittest
from solver import Node, largest_bst

class TestSolver(unittest.TestCase):
  def test_largest_bst(self):
    # BST on root + left branch
    root = Node(5, Node(4, Node(3), Node(7)), Node(6, Node(8), Node(9)))
    self.assertEqual(largest_bst(root), 3)

    # BST on root + right branch
    root = Node(5, Node(4, Node(6), Node(7)), Node(6, Node(2), Node(8)))
    self.assertEqual(largest_bst(root), 3)

    # Full tree is a BST
    root = Node(5, Node(4, Node(2, Node(0), Node(3)), Node(6)), Node(6))
    self.assertEqual(largest_bst(root), 4)

    # BST on a subtree in the left node
    root = Node(5, Node(8, Node(4, Node(1)), Node(9)), Node(9, Node(10), Node(11)))
    self.assertEqual(largest_bst(root), 3)

    # BST on a subtree in the right node
    root = Node(5, Node(8, Node(10), Node(11)), Node(4, Node(2, Node(1)), Node(6)))
    self.assertEqual(largest_bst(root), 3)

    # No subtree is a BST
    root = Node(5, Node(6, Node(9), Node(5)), Node(4, Node(6), Node(2)))
    self.assertEqual(largest_bst(root), 1) # Any leaf is a BST by definition

    # Root with no children
    root = Node(1)
    self.assertEqual(largest_bst(root), 1)

    # Root is 'None'
    root = None
    self.assertEqual(largest_bst(root), 0)

if __name__ == "__main__":
    unittest.main()
