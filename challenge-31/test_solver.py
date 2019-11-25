import unittest
from solver import Node, has_cycle

class TestSolver(unittest.TestCase):
  def test_connected_graph(self):
    a, b, c = [Node('a'), Node('b'), Node('c')]
    a.add_edge(b)
    b.add_edge(c)
    self.assertFalse(has_cycle([a,b,c]))

    c.add_edge(a)
    self.assertTrue(has_cycle([a,b,c]))

  def test_disconnected_graph(self): 
    a, b, c, d, e = [Node('a'), Node('b'), Node('c'), Node('d'), Node('e')]
    
    # First cluster (no cycle)
    a.add_edge(b) 
    
    # Second cluster (with cycle)
    c.add_edge(d)
    d.add_edge(e)
    e.add_edge(c)

    self.assertTrue(has_cycle([a,b,c,d,e]))

if __name__ == "__main__":
    unittest.main()
