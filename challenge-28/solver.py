class Node(object):
  def __init__(self, v, left=None, right=None):
    self.v = v
    self.left = left
    self.right = right

def is_bst(root):
  return helper(root, float('-inf'), float('inf'))

def helper(node, lower, upper):
  # Null node: is a bst by default
  if not node:
    return True

  # Check bst with immediate children
  if lower >= node.v or upper <= node.v:
    return False

  # Check if left branch is a bst
  if not helper(node.left, lower, node.v):
    return False

  # Check if right branch is a bst
  if not helper(node.right, node.v, upper):
    return False

  return True
