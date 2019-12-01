def sudoku(board, rows, columns):
  return helper(board, 0, 0, columns, rows)

def helper(board, r, c, rows, columns):
  def inbound(r, c):
    return (0 <= r < rows) and (0 <= c < columns)

  # Out of bounds:
  # We filled all blank cells and, thus, a valid solution
  if not inbound(r, c):
    return True

  nr, nc = next_pos(r, c, rows, columns)

  if board[r][c] != 0:
    # This is a pre-filled cell, so skip
    # for the next one
    return helper(board, nr, nc, rows, columns)

  for i in range(1, 10):
    if valid_placement(board, r, c, rows, columns, i):
      # "i" can be place in the cell without breaking
      # the sudoku rules. So, it's a canditate for solution.
      # Mark the cell with the value and try to solve
      # recursively for the remaining blank cells
      board[r][c] = i

      if helper(board, nr, nc, rows, columns):
        return True
      else:
        # No solution found for the search branch:
        # reset the cell for the future attemps
        board[r][c] = 0

  return False

def next_pos(r, c, rows, columns):
  if c + 1 == columns:
    return (r + 1, 0)
  else:
    return (r, c + 1)

def valid_placement(board, r, c, rows, columns, v):
  # Check conflict with row
  if v in board[r]:
    return False

  # Check conflict with column
  for i in range(0, rows):
    if v == board[i][c]:
      return False

  # Check conflict with the subgrid
  row_offset = r - r % 3
  col_offset = c - c % 3

  for i in range(3):
    for j in range(3):
      if board[i + row_offset][j + col_offset] == v:
        return False

  return True
