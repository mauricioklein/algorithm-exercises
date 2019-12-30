PLUS   = '+'
MINUS  = '-'
TIMES  = '*'
DIVIDE = '/'

class Node(object):
  def __init__(self, v, left=None, right=None):
    self.v = v
    self.left = left
    self.right = right

  def is_operation(self):
    return self.v in (PLUS, MINUS, TIMES, DIVIDE)

#
# Time  complexity: O(n)    (each node is evaluate at most once)
# Space complexity: O(logn) (depth of the tree)
#
def evaluate(node):
  if node.is_operation():
    left  = evaluate(node.left)
    right = evaluate(node.right)

    return left + right if node.v == PLUS  else \
           left - right if node.v == MINUS else \
           left * right if node.v == TIMES else \
           left / right
  else:
    return node.v
