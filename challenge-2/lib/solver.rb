class Solver
  def call(arr)
    return [] if arr.empty?

    max = arr.max
    fib_lookup = generate_fib_lookup(max)
    result = []

    arr.each do |val|
      if fib_lookup.has_key?(val)
        result << val
      end
    end

    result
  end

  private

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
