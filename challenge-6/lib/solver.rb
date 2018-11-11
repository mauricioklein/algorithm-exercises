class Solver
  NULL_NODE = "-"

  def serialize(root)
    to_string(root)
  end

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
