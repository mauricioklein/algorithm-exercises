def witnesses(people):
  """
  Time complexity: O(n)
  Space complexity: O(1)
  """
  N = len(people)
  tallest, witnesses_count = 0, 0

  for i in range(N - 1, -1, -1):
    height = people[i]

    if height > tallest:
      witnesses_count += 1
      tallest = height

  return witnesses_count
