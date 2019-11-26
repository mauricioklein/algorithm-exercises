RIGHT = 1
DOWN  = 2
LEFT  = 3
UP    = 4

#
# Time  complexity: O(n*m)
# Space complexity: O(n*m) (result array)
#
def spiral_traverse(arr, n_rows, m_columns):
  def inbounds(row, column):
    return (0 <= row < n_rows) and (0 <= column < m_columns)

  matrix = to_matrix(arr, n_rows, m_columns)
  result = []

  row, column, direction = 0, 0, RIGHT

  for _ in range(n_rows * m_columns):
    # Visit the cell
    result.append(matrix[row][column])
    matrix[row][column] = None

    # Check if we need to change directions
    nr, nc = next_step(direction, row, column)
    if not inbounds(nr, nc) or matrix[nr][nc] == None:
      direction = next_direction(direction)

    row, column = next_step(direction, row, column)

  return result

def next_step(direction, row, column):
  return {
    RIGHT: (row    , column + 1),
    DOWN : (row + 1, column    ),
    LEFT : (row    , column - 1),
    UP   : (row - 1, column    )
  }[direction]

def next_direction(current_direction):
  return {
    RIGHT: DOWN,
    DOWN : LEFT,
    LEFT : UP,
    UP   : RIGHT
  }[current_direction]

def to_matrix(arr, rows, columns):
  matrix = [ [ 0 for i in range(columns) ] for j in range(rows) ]

  for i in range(columns):
    for j in range(rows):
      matrix[i][j] = arr[i * rows + j]

  return matrix
