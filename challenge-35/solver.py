#
# Time complexity: O(n^2)
# Space complexity: O(n/2) (worst case, where we've distinct vertical lines)
#
def count_rectangles(points):
  vertical_lines = {}

  for p1 in points:
    for p2 in points:
      # Same points don't make a line
      if p1 == p2:
        continue

      if stacked(p1, p2):
        point = make_point(p1, p2)
        vertical_lines[point] = vertical_lines.get(point, 0) + 1

  acc = 0
  for count in vertical_lines.values():
    # We need at least two vertical lines to make a rectangle
    if count < 2:
      continue

    acc += 1 if count == 2 else count

  return acc

def make_point(p1, p2):
  p1_y, p2_y = p1[1], p2[1]

  return (
    min(p1_y, p2_y), 
    max(p1_y, p2_y)
  )


def stacked(p1, p2):
  p1_x, p1_y = p1
  p2_x, p2_y = p2

  if p1_x != p2_x:
    return False

  return p1_y < p2_y
