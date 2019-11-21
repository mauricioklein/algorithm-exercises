class Solver
  #
  # Time complexity:  O(n) ("n" to calculate the array product + "n" to calculate the product for every element)
  # Space complexity: O(n) (requires a new array for the result)
  #
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
