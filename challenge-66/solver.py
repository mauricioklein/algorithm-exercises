class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

"""
  Time  complexity: O(n) (where n = number of elements in the tree)
  Space complexity: O(n) (for the output array)
"""
def level_order(root):
  if not root:
    return []

  queue = [root]
  output = []

  while queue:
    node = queue.pop(0)

    output.append(node.val)

    if node.left:
      queue.append(node.left)

    if node.right:
      queue.append(node.right)

  return output
