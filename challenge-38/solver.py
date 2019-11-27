class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)

#
# Time  complexity: O(n)
# Space complexity: O(1)
#
def remove_kth_last(head, k):
  # Place "right" on the kth + 1 element of the list
  right = head

  for _ in range(k):
    right = right.next

  # Move "left" and "right" together, while keeping track of the left's previous node ("prev"),
  # until "right" reaches the end of the list.
  # In this moment, "left" will be on the kth last element and "prev" on the node
  # imediately before
  prev, left = None, head

  while right is not None:
    prev = left
    left = left.next
    right = right.next

  if prev == None:
    # We're removing the first element, so return
    # the second element as the new "head"
    return left.next
  else:
    # Remove the kth last element
    prev.next = left.next
    return head
