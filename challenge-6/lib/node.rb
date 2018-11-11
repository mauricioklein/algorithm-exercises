class Node
  attr_reader :val, :left, :right

  def initialize(val, left = nil, right = nil)
    @val   = val
    @left  = left
    @right = right
  end
end
