import unittest
import solver
from solver import Node, values_at_height

class TestSolver(unittest.TestCase):
  def test_values_at_height(self):
    root = Node(1)
    self.assertEqual(values_at_height(root, 1), [1])

    root = Node(1, Node(2), Node(3))
    self.assertEqual(values_at_height(root, 2), [2, 3])
    
    root = Node(1, Node(3))
    self.assertEqual(values_at_height(root, 2), [3])

    root = Node(1, Node(2), Node(3))
    self.assertEqual(values_at_height(root, 5), [])

    root = Node(1, Node(2, Node(4), Node(5)), Node(3, right=Node(7)))
    self.assertEqual(values_at_height(root, 3), [4, 5, 7])
    
if __name__ == "__main__":
    unittest.main()
