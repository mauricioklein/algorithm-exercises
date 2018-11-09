class Solver
  def call(arr)
    total = arr.reduce(:*)
    result = Array.new(arr.length)

    arr.each_with_index do |val, i|
      # With division
      result[i] = total / val

      # Without division
      # result[i] = total * (val ** -1)
    end

    result
  end
end
