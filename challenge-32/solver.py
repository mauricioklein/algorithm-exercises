class Node(object):
  def __init__(self, V):
    self.V = V
    self.edges = {}

  def add_edge(self, node, cost):
    self.edges[node] = cost

class Graph(object):
  def __init__(self, vertices):
    self.vertices = {
      n: {
        'distance': float('inf'),
        'previous': None,
        'visited' : False
      } for n in vertices
    }

  def min_distance(self):
    min_dist = float('inf')
    node = None

    for v in self.vertices:
      if not self.is_visited(v) and self.get_distance(v) < min_dist:
        min_dist = self.get_distance(v)
        node = v

    return node

  def is_visited(self, node):
    return self.vertices[node]['visited']

  def mark_as_visited(self, node):
    self.vertices[node]['visited'] = True

  def get_distance(self, node):
    return self.vertices[node]['distance']

  def set_distance(self, node, distance):
    self.vertices[node]['distance'] = distance

  def set_previous(self, node, previous):
    self.vertices[node]['previous'] = previous

  def get_previous_from(self, node):
    return self.vertices[node]['previous']

  def dijkstra(self, source):
    # Initialize source with zero distance
    self.set_distance(source, 0)

    node = self.min_distance()

    while node:
      for edge, edge_distance in node.edges.items():
        if self.is_visited(edge):
          continue

        # Calculate the distance to the edge and, if shorter,
        # updates the vertex distance and previous node
        d = self.get_distance(node) + edge_distance
        if d < self.get_distance(edge):
          self.set_distance(edge, d)
          self.set_previous(edge, node)

      self.mark_as_visited(node)
      node = self.min_distance()

  def shortest_path(self, source, target):
    self.dijkstra(source)

    path, node = [], target
    while node:
      path.append(node)
      node = self.get_previous_from(node)

    path.reverse()

    return path
