class Solver
  #
  # Time complexity:  O(n^2) ("n" lines * "n columns")
  # Space complexity: O(1) (matrix rotated in place)
  #
  def call(table)
    m = table.length

    for i in (0..(m/2) - 1)
      for j in (i..(m - i - 2))
        rotate(table, i, j, m)
      end
    end

    table
  end

  private

  def rotate(table, i, j, m)
    offset = m - 1

    x = table[i][j]

    table[i         ][j         ] = table[j         ][offset - i]
    table[j         ][offset - i] = table[offset - i][offset - j]
    table[offset - i][offset - j] = table[offset - j][i         ]
    table[offset - j][i         ] = x
  end
end
