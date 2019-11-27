import unittest
from solver import Node, remove_kth_last

class TestSolver(unittest.TestCase):
  def test_remove_middle(self):
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    self.assertEqual(str(head), "[1, 2, 3, 4, 5]")
    
    head = remove_kth_last(head, 3)
    self.assertEqual(str(head), "[1, 2, 4, 5]")

  def test_remove_last(self):
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    self.assertEqual(str(head), "[1, 2, 3, 4, 5]")
    
    head = remove_kth_last(head, 1)
    self.assertEqual(str(head), "[1, 2, 3, 4]")

  def test_remove_first(self):
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    self.assertEqual(str(head), "[1, 2, 3, 4, 5]")
    
    head = remove_kth_last(head, 5)
    self.assertEqual(str(head), "[2, 3, 4, 5]")

if __name__ == "__main__":
    unittest.main()
