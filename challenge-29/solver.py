#
# Time complexity: 
#   O(lines*columns) (worst case, where all the neighbours have the same color)
#   O(1)             (best case, where no neighbour has the same color)
#
# Space complexity:
#   O(1) (color changes applied in place)
#
def flood_fill(screen, lines, columns, line, column, color):
  def inbound(l, c):
    return (l >= 0 and l < lines) and (c >= 0 and c < columns)

  def key(l, c):
    return "{},{}".format(l, c)

  stack = [[line, column]]
  visited = set()

  while stack:
    l, c = stack.pop()

    # Mark the cell as visited
    visited.add(key(l, c))

    # Schedule the visit to all neighbours (except diagonal),
    # which weren't visited yet and has the same color
    neighbours = [
      [l-1, c  ], 
      [l+1, c  ], 
      [l  , c-1], 
      [l  , c+1]
    ]

    for nl, nc in neighbours:
      if inbound(nl, nc) and key(nl, nc) not in visited and screen[nl][nc] == screen[l][c]:
        stack.append([nl, nc])
      
    # Paint the current cell
    screen[l][c] = color

  return screen
