class Node(object):
  def __init__(self, v, left=None, right=None):
    self.v = v
    self.left = left
    self.right = right

#
# Time  complexity: O(n) (every element is visited at most once)
# Space complexity: O(n) (worst case, considering "height" equal to the tree's depth)
#
def values_at_height(node, height):
  if not node:
    return []

  if height == 1:
    return [node.v]
  else:
    left  = values_at_height(node.left,  height - 1)
    right = values_at_height(node.right, height - 1)

    return left + right
