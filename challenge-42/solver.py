class Node(object):
  def __init__(self):
    self.left = self.right = None

  def __str__(self):
    left  = '0' if self.left  == None else str(self.left )
    right = '0' if self.right == None else str(self.right)

    return "({}{})".format(left, right)

#
# Time  complexity: O(n+m) (where "n" is the string length and "m" is the number of nodes in the tree)
# Space complexity: O(m)   (for the tree representation)
#
def tree_depth(stringified_tree):
  # 1. Transform string into a tree
  stack = []

  for char in stringified_tree:
    if char == '(':
      stack.append(Node())
    elif char == '0':
      stack.append(None)
    elif char == ')':
      right, left, root = stack.pop(), stack.pop(), stack.pop()

      root.left = left
      root.right = right

      stack.append(root)

  # 2. Calculate the depth from the root
  root = stack.pop()
  return depth(root)

def depth(node):
  if not node:
    return 0

  return 1 + max(depth(node.left), depth(node.right))
