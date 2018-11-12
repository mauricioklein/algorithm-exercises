class Solver
  def call(table, n_lines, n_columns)
    lookup = {}
    helper(table, 0, 0, n_lines, n_columns, lookup)
  end

  private

  def helper(table, line, column, n_lines, n_columns, lookup)
    return 0 if (line == n_lines || column == n_columns)

    s1 =    sum(table, line    , column    , n_lines, n_columns, lookup)
    s2 = helper(table, line    , column + 1, n_lines, n_columns, lookup)
    s3 = helper(table, line + 1, column    , n_lines, n_columns, lookup)
    s4 = helper(table, line + 1, column + 1, n_lines, n_columns, lookup)

    max(s1, s2, s3, s4)
  end

  def sum(table, line, column, n_lines, n_columns, lookup)
    pair = [line, column]

    return lookup[pair] if lookup.has_key?(pair)

    next_line   = line   + 1 < n_lines
    next_column = column + 1 < n_columns

    s1 = table[line][column]
    s2 = (next_line               ) ? table[line+1][column  ] : 0
    s3 = (next_column             ) ? table[line  ][column+1] : 0
    s4 = (next_line && next_column) ? table[line+1][column+1] : 0

    (s1 + s2 + s3 + s4).tap do |result|
      lookup[pair] = result
    end
  end

  def max(*values)
    values.max
  end
end
