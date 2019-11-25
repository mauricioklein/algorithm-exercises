import unittest
from solver import Graph, Node

class TestSolver(unittest.TestCase):
  def test_connected_graph(self):
    a, b, c, d, e = Node('a'), Node('b'), Node('c'), Node('d'), Node('e')

    source, target = a, e

    # First path (distance: 30)
    a.add_edge(b, 10); b.add_edge(a, 10);
    b.add_edge(c, 10); c.add_edge(b, 10);
    c.add_edge(e, 10); e.add_edge(c, 10);

    # Second path (distance: 35)
    a.add_edge(d, 25); d.add_edge(a, 25);
    d.add_edge(e, 10); e.add_edge(d, 10);

    g = Graph([a,b,c,d,e])

    self.assertEqual(g.shortest_path(a, e), [a, b, c, e])

if __name__ == "__main__":
    unittest.main()
