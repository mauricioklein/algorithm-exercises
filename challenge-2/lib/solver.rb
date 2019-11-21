class Solver
  #
  # Time complexity:  O(n) ("n" to find the max element + "n" for generate the fib lookup + "n" to traverse the array)
  # Space complexity: O(n) ("n" for the fib lookup + "n" for the result array)
  #
  def call(arr)
    return [] if arr.empty?

    max = arr.max # Time complexity: O(n)
    fib_lookup = generate_fib_lookup(max) # Time complexity: O(n)

    # Time complexity: O(n)
    arr.each do |val|
      if fib_lookup.has_key?(val)
        result << val
      end
    end

    result
  end

  private

  #
  # Time complexity:  O(n) (grows linearly with the max element)
  # Space complexity: O(n) (requires a hash to store the fib values)
  #
  def generate_fib_lookup(max)
    lookup = {
      0 => nil,
      1 => nil
    }

    first, second = 1, 1
    next_val = nil

    while second < max
      next_val = first + second
      lookup[next_val] = nil

      first = second
      second = next_val
    end

    lookup
  end
end
