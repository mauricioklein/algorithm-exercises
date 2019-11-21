class Solver
  NULL_NODE = "-"

  #
  # Time complexity:  O(n) (regular binary tree traversal)
  # Space complexity: O(1) (only a string for the result is required)
  #
  def serialize(root)
    to_string(root)
  end

  #
  # Time complexity:  O(n) (regular binary tree construction)
  # Space complexity: O(n) (for the splitted serialized tree)
  #
  def deserialize(serialized_root)
    from_string(serialized_root.split(/ /), 0).first
  end

  private

  def to_string(node)
    return NULL_NODE if node.nil?

    val   = node.val
    left  = to_string(node.left)
    right = to_string(node.right)

    "#{val} #{left} #{right}"
  end

  def from_string(elements, index)
    return [nil, index] if elements[index] == NULL_NODE

    val = elements[index]
    left,  next_index = from_string(elements, index      + 1)
    right, next_index = from_string(elements, next_index + 1)

    [
      Node.new(val, left, right),
      next_index
    ]
  end
end
