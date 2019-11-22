import unittest
from solver import Node, is_bst

class TestSolver(unittest.TestCase):
  def test_is_bst(self):
    root = Node(5, Node(1), Node(4, Node(3), Node(6)))
    self.assertFalse(is_bst(root))

    root = Node(5, Node(3, Node(2), Node(4)), Node(7, Node(6), Node(8)))
    self.assertTrue(is_bst(root))

    root = Node(0)
    self.assertTrue(is_bst(root))

    root = Node(2, Node(1))
    self.assertTrue(is_bst(root))

    root = Node(2, right=Node(3))    
    self.assertTrue(is_bst(root))

if __name__ == "__main__":
    unittest.main()
