require_relative 'node'

class Solver
  def call(ternary_if)
    stack = []
    index = 0

    while index < ternary_if.length
      ch = ternary_if[index]

      if letter?(ch)
        stack << Node.new(ch)
      elsif ch == ':'        
        right = Node.new(ternary_if[index + 1])
        left = stack.pop
        root = stack.pop

        root.left = left
        root.right = right
        stack << root

        index += 1
      end

      index += 1
    end

    stack.pop.to_s
  end

  private

  def letter?(ch)
    ('A'..'Z').include?(ch.upcase)
  end
end
