class Queue:
  def __init__(self):
    self.main_stack = []
    self.aux_stack  = []
   
  #
  # Time complexity: O(n) 
  #
  def enqueue(self, val):
    # Move all elements from the main stack
    # to the aux stack
    while self.main_stack:
      self.aux_stack.append(
        self.main_stack.pop()
      )

    # Add the element to the inverted stack
    self.aux_stack.append(val)

    # Move elements back to the main stack
    while self.aux_stack:
      self.main_stack.append(
        self.aux_stack.pop()
      )

  #
  # Time complexity: O(1)
  #
  def dequeue(self):
    return self.main_stack.pop()
