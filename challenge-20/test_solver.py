import unittest
from solver import ListNode

class TestSolver(unittest.TestCase):
    def test_solver_iteratively(self):
        # Create nodes
        nodes = [
            ListNode(4),
            ListNode(3),
            ListNode(2),
            ListNode(1)
        ]

        # Chain the nodes
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[len(nodes)-1].next = None

        # Reverse the list
        head = nodes[0]
        head.reverseIteratively(head)

        # Verify
        node = nodes[len(nodes)-1]
        for i in range(1,5):
            self.assertEqual(node.val, i)
            node = node.next

    def test_solver_recursively(self):
        # Create nodes
        nodes = [
            ListNode(4),
            ListNode(3),
            ListNode(2),
            ListNode(1)
        ]

        # Chain the nodes
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[len(nodes)-1].next = None

        # Reverse the list
        head = nodes[0]
        head.reverseRecursively(head)

        # Verify
        node = nodes[len(nodes)-1]
        for i in range(1,5):
            self.assertEqual(node.val, i)
            node = node.next
  
if __name__ == "__main__":
    unittest.main()
