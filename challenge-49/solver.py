#
# Time  complexity: O(n) (where "n" is the length of any of the strings)
# Space complexity: O(1)
#
def buddy_strings(a, b):
  # Check string length match
  if len(a) != len(b):
    return False

  # Check if same string with duplicated characters
  if a == b and len(a) > len(set(a)):
    return True

  # Calculate the diff between the strings
  diff_a, diff_b = [], []
  for i in range(len(a)):
    if a[i] != b[i]:
      diff_a.append(a[i])
      diff_b.append(b[i])

      if len(diff_a) > 2:
        return False

  # We expect exactly two diffs to make one swap
  # So, if the number of diffs is different of two, more or
  # less than one swap is needed and, thus, "false"
  if len(diff_a) != 2:
    return False

  # Check if the swaps match
  if diff_a[0] != diff_b[1] or diff_a[1] != diff_b[0]:
    return False

  return True
