from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''
    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.value)
      nodes.append(node.left)
      nodes.append(node.right)
    return answer

def create_balanced_bst(nums):
  if not nums:
    return None

  mid = len(nums) // 2

  return Node(
    nums[mid],
    left = create_balanced_bst(nums[:mid]),
    right = create_balanced_bst(nums[mid+1:])
  )
