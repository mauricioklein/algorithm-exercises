class Node
  attr_reader   :value
  attr_accessor :left, :right

  def initialize(value)
    @value = value
  end

  def to_s
    "(#{left.to_s} < #{value} > #{right.to_s})"
  end
end
