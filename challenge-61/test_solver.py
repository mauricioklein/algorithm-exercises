import unittest
from solver import Node, full_binary_tree

class TestSolver(unittest.TestCase):
  def test_full_binary_tree(self):
    #     1               1
    #    / \             / \
    #   2   3    ---->  0   3
    #  /   / \             / \
    # 0   9   4           9   4
    root = Node(1, Node(2, Node(0)), Node(3, Node(9), Node(4)))
    expected_str_output = "1\n03\n94"

    self.assertEqual(str(full_binary_tree(root)), expected_str_output)

    #     1                1
    #    / \              / \
    #   3   2    ---->   3   4
    #  / \   \          / \
    # 0   9   4        0   9
    root = Node(1, Node(3, Node(0), Node(9)), Node(2, right=Node(4)))
    expected_str_output = "1\n34\n09"

    self.assertEqual(str(full_binary_tree(root)), expected_str_output)

    #   1         3
    #  /   ---->
    # 3
    root = Node(1, Node(3))
    expected_str_output = "3"

    self.assertEqual(str(full_binary_tree(root)), expected_str_output)

    #   1           3
    #    \   ---->
    #     3
    root = Node(1, right=Node(3))
    expected_str_output = "3"

    self.assertEqual(str(full_binary_tree(root)), expected_str_output)

if __name__ == "__main__":
    unittest.main()
