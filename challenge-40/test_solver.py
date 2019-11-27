import unittest
from solver import Queue

class TestSolver(unittest.TestCase):
  def test_queue(self):
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    self.assertEqual(q.dequeue(), 1)
    self.assertEqual(q.dequeue(), 2)
    self.assertEqual(q.dequeue(), 3)

if __name__ == "__main__":
    unittest.main()
