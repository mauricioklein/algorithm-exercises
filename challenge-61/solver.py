from collections import deque

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      num = len(q)
      while num > 0:
        n = q.popleft()
        result += str(n.value)
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
        num = num - 1
      if len(q):
        result += "\n"

    return result

def full_binary_tree(node):
  if not node:
    return None

  left  = full_binary_tree(node.left)
  right = full_binary_tree(node.right)

  if (left and right) or (not left and not right):
    node.left  = left
    node.right = right
    return node
  else:
    return left or right
