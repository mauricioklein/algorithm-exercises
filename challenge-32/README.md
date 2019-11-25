# Shortest path in a indirected acyclic graph

## Description

Given a weighted graph, a source node and a target node, find the shortest distance between these two nodes

## Example

```
Input:
  a, b, c, d, e = Node('a'), Node('b'), Node('c'), Node('d'), Node('e')

  source, target = a, e

  # First path (distance: 30)
  a.add_edge(b, 10)
  b.add_edge(c, 10)
  c.add_edge(e, 10)

  # Second path (distance: 35)
  a.add_edge(d, 25)
  d.add_edge(e, 10)

  Graph([a,b,c,d,e]).shortest_path(a,e) # [a, b, c, e]
```
