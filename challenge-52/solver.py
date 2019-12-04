class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val

def deepest(node):
  if not node.left and not node.right:
    return(node, 1)
  elif not node.left:
    return inc_tuple(deepest(node.right))
  elif not node.right:
    return inc_tuple(deepest(node.left))
  else:
    return inc_tuple(
      max(
        deepest(node.left),
        deepest(node.right),
        key=lambda t: t[1]
      )
    )

def inc_tuple(t):
  node, depth = t
  return (node, depth+1)
