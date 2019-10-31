class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

  # Function to print the list
  def printList(self):
    node = self
    output = ''
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    prev = head
    cur = head.next

    while cur:
        _next, cur.next = cur.next, prev
        prev, cur = cur, _next
        
    head.next = None

  def reverseRecursively(self, head):
      if not head or not head.next:
          return head

      node = self.reverseRecursively(head.next)
      head.next.next = head
      head.next = None
      return node
