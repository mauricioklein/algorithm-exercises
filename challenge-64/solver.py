"""
  Time  complexity: O(n*m) (where n = nth sequence, m = length of the longest sequence)
  Space complexity: O(m)   (for the resulting sequence)
"""
def look_and_say(n):
  sequence = "1"

  for _ in range(n - 1):
    sequence = "".join(groups(sequence))

  return sequence

"""
Return an array with pairs [occurrences, char]
Ex:
  "1122212" = [["2", "1"], ["3", "2"], ["1", "1"], ["1", "2"]]
"""
def groups(word):
  groups = []
  last_char, count = None, 0

  for char in word:
    if not last_char:
      last_char, count = char, 1
    else:
      if char == last_char:
        count += 1
      else:
        groups.extend([str(count), last_char])
        last_char, count = char, 1

  # Remaining
  groups.extend([str(count), last_char])

  return groups
