# Find cycle in indirected graph

This questions was asked by Amazon.

## Description

Given a list of vertices in a graph, implement a function that detects cycles in this graph.

## Example

```
Input:
  a, b, c = Node('a'), Node('b'), Node('c')
  a.add_edge(b)
  b.add_edge(c)

  has_cycle([a,b,c]) # False

  c.add_edge(a)
  has_cycle([a,b,c]) # True
```
