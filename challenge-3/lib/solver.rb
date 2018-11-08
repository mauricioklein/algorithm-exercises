class Solver
  def call(arr, k)
    lookup = {}

    for i in (0..arr.length - 1)
      pair = k - arr[i]

      return true if lookup.has_key?(pair)

      lookup[arr[i]] = nil
    end

    false
  end
end
