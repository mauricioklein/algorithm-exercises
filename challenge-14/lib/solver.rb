require_relative "./tries"

class Solver
  def call(dict, word)
    return [] if word.empty?

    tries = DictionaryTries.build_from(dict)
    node = find_last_node_for_word(tries, word)

    return [] if node.nil?

    aggregate_children(node)
  end

  private

  def find_last_node_for_word(tries, word)
    node = tries.root

    word.split(//).each do |letter|
      next_node = node.find(letter)

      return nil if next_node.nil?

      node = next_node
    end

    node
  end

  def aggregate_children(root)
    words = []
    stack = [root]

    while !stack.empty?
      node = stack.pop

      if node.leaf?
        words << node.word
      end

      node.children.each do |child|
        stack << child
      end
    end

    words
  end
end
