class Node(object):
  def __init__(self, vertex):
    self.vertex = vertex
    self.edges = []

  def add_edge(self, edge):
    self.edges.append(edge)
    edge.edges.append(self)

#
# Time complexity:  O(n) (every node is visited at most once)
# Space complexity: O(n) (stack to define the traversal path)
#
def has_cycle(vertices):
  visited = set()

  for v in vertices:
    # Vertice was already visited by another node,
    # so we can skip
    if v in visited:
      continue

    if helper(v, visited):
      return True

  return False

def helper(root, visited):
  stack = [[root, None]] # Pair "[node, parent]"

  while stack:
    node, parent = stack.pop()

    # Visit the node
    visited.add(node)

    # Schedule the visit for all non-visited edges
    for edge in node.edges:
      if edge in visited:
        if edge is not parent:
          # Found a cycle
          return True
      else:
        stack.append([edge, node])

  return False
