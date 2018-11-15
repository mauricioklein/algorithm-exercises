class Solver
  def call(code)
    count_decodes(code, 0)
  end

  private

  def count_decodes(code, index)
    return 1 if index >= (code.length - 1)

    count = 0

    # Check if the first char is decodable
    if decodable?(code[index])
      count += count_decodes(code, index + 1)
    end

    # Check if the first two chars together
    # is decodable
    if decodable?(code[index..index+1])
      count += count_decodes(code, index + 2)
    end

    count
  end

  def decodable?(ch)
    (1..27).include?(ch.to_i)
  end
end
