def find_ranges(nums):
  if not nums:
    return []

  first = last = nums[0]
  ranges = []

  def append_range(first, last):
    ranges.append('{}->{}'.format(first, last))

  for num in nums:
    if abs(num - last) > 1:
      append_range(first, last)
      first = num

    last = num

  # Remaining
  append_range(first, last)

  return ranges
