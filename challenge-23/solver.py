class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

  def string(self):
    buffer = self.value

    if self.left: buffer += self.left.string()
    if self.right: buffer += self.right.string()

    return buffer

class Solution:
  def invert_recursively(self, node):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if node:
      node.left, node.right = self.invert_recursively(node.right), self.invert_recursively(node.left)

    return node

  def invert_iteratively(self, root):
    """
    Time complexity: O(n)
    Space complexity: O(n) (requires a stack)
    """
    stack = [root]

    while len(stack) > 0:
      n = stack.pop()

      n.left, n.right = n.right, n.left

      if n.left:  stack.append(n.left)
      if n.right: stack.append(n.right)

    return root
