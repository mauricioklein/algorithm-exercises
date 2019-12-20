
#
# Time complexity : O(n*m) (where n = rows in the grid, m = columns in the grid)
# Space complexity: O(n*m) (worst case, when all the positions are land and the walk goes recursively to all positions)
#
def count_islands(grid):
  rows, columns = len(grid), len(grid[0])
  islands = 0

  for row in range(rows):
    for column in range(columns):
      if grid[row][column] == 1:
        islands += 1
        walk(grid, (row, column), (rows, columns))

  return islands

#
# walk marks the cell (pos) + all non-visited neighbours
# as visited (cell value = 2)
#
def walk(grid, pos, dimensions):
  r, c = pos
  rows, columns = dimensions

  def inbounds(row, column):
    return (0 <= row < rows) and (0 <= column < columns)

  # Mark the current position as visited
  grid[r][c] = 2

  # Mark the non-visited land neighbours as visited
  paths = [(-1,0), (1,0), (0,-1), (0,1)]

  for path in paths:
    nr = r + path[0]
    nc = c + path[1]

    if inbounds(nr, nc) and grid[nr][nc] == 1:
      walk(grid, (nr, nc), dimensions)
