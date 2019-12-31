#
# Time  complexity: O(n)
# Space complexity: O(1) (sort performed in place)
#
def sort_colors(colors):
  def swap(i, j):
    colors[i], colors[j] = colors[j], colors[i]

  left, right = 0, len(colors) - 1
  i = 0

  while i <= right:
    if colors[i] == 0:
      swap(i, left)
      left += 1
      i += 1
    elif colors[i] == 2:
      swap(i, right)
      right -= 1
    else:
      i += 1

  return colors
