class Solver
  #
  # Time complexity:  O(n) (traverse the matrix once)
  # Space complexity: O(n) (requires a new matrix for the result)
  #
  def call(arr, n_rows, n_columns)
    length = n_rows * n_columns

    row, col = 0, 0
    inc_row, inc_col = 0, 1

    result = Array.new(length)

    length.times do |pos|
      offset = calculate_offset(row, col, n_columns)

      # Assign the element to result and
      # mark the cell as visited (= nil)
      result[pos] = arr[offset]
      arr[offset] = nil

      # If found a wall (end of array or visited cell),
      # turn the walk diretion to the right
      if wall?(arr, row + inc_row, col + inc_col, n_columns, n_rows)
        inc_row, inc_col = turn_right(inc_row, inc_col)
      end

      # Update indexes
      row += inc_row
      col += inc_col
    end

    result
  end

  private

  #
  # Time complexity:  O(1)
  # Space complexity: O(1)
  #
  def calculate_offset(row, col, n_columns)
    n_columns * row + col
  end

  #
  # Time complexity:  O(1)
  # Space complexity: O(1)
  #
  def wall?(arr, row, col, n_columns, n_rows)
    outbound?(row, n_rows) || outbound?(col, n_columns) || arr[calculate_offset(row, col, n_columns)].nil?
  end

  #
  # Time complexity:  O(1)
  # Space complexity: O(1)
  #
  def outbound?(i, length)
    i < 0 || i >= length
  end

  #
  # Time complexity:  O(1)
  # Space complexity: O(1)
  #
  def turn_right(inc_row, inc_col)
    return [ 1,  0] if inc_col == 1
    return [ 0, -1] if inc_row == 1
    return [-1,  0] if inc_col == -1
           [ 0,  1]
  end
end
