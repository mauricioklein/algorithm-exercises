class DictionaryTries
  def self.build_from(dictionary)
    new.tap do |klass|
      klass.parse(dictionary)
    end
  end

  attr_reader :root

  def initialize
    @root = Node.new("")
  end

  def parse(dictionary)
    dictionary.each do |word|
      cur_node = root
      cur_word = ""

      word.split(//).each do |letter|
        cur_word += letter
        next_node = cur_node.find(letter)

        if next_node.nil?
          next_node = cur_node.add(cur_word)
        end

        cur_node = next_node
      end
    end
  end

  class Node
    attr_accessor :word, :children_map

    def initialize(word)
      @word = word
      @children_map = {}
    end

    def children
      children_map.values
    end

    def add(word)
      Node.new(word).tap do |node|
        children_map[word[-1]] = node
      end
    end

    def find(letter)
      children_map[letter]
    end

    def leaf?
      children.empty?
    end
  end
end
