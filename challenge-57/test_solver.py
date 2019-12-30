import unittest
import solver
from solver import Node, evaluate

class TestSolver(unittest.TestCase):
  def test_evaluate(self):
    # Single sum: (15 + 5)
    root = Node(solver.PLUS, Node(15), Node(5))
    self.assertEqual(evaluate(root), 20)
    
    # Single subtraction: (15 - 5)
    root = Node(solver.MINUS, Node(15), Node(5))
    self.assertEqual(evaluate(root), 10)

    # Single multiplication: (15 * 5)
    root = Node(solver.TIMES, Node(15), Node(5))
    self.assertEqual(evaluate(root), 75)

    # Single division: (15 / 5)
    root = Node(solver.DIVIDE, Node(15), Node(5))
    self.assertEqual(evaluate(root), 3)

    # Chained operations: (3 + 2) * (4 + 5)
    root = Node(solver.TIMES, Node(solver.PLUS, Node(3), Node(2)), Node(solver.PLUS, Node(4), Node(5)))
    self.assertEqual(evaluate(root), 45)

if __name__ == "__main__":
    unittest.main()
