class Node(object):
  def __init__(self, v, left=None, right=None):
    self.v = v
    self.left = left
    self.right = right

#
# Time  complexity: O(n) (check every node at most once)
# Space complexity: O(n) (for the recursion tree)
#
def largest_bst(root):
  return helper(root, 0)

def helper(node, acc_depth):
  # Found the end of the subtree
  if not node:
    return acc_depth

  # Check if node is a valid BST
  is_bst = (node.left  == None or node.left.v  < node.v) and \
           (node.right == None or node.right.v > node.v)

  # If the current node is a BST, recurse with an incremented
  # accumulated depth, otherwise, reset it.
  acc_depth = acc_depth + 1 if is_bst else 0

  return max(helper(node.left,  acc_depth), 
             helper(node.right, acc_depth))
