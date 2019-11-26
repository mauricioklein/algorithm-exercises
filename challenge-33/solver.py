#
# Time  complexity: O(n*log(n)) (for the sort)
# Space complexity: O(n)        (for the result array)
#
def merge_overlapping_intervals(intervals):
  # Sort intervals by start timestamp
  intervals.sort(key=lambda interval: interval[0])

  merged_intervals = []

  for interval in intervals:
    if merged_intervals and overlap(merged_intervals[-1], interval):
      merged_intervals[-1] = merge(merged_intervals[-1], interval)
    else:
      merged_intervals.append(interval)

  return merged_intervals

def overlap(prev_i, next_i):
  start, end = next_i[0], prev_i[1]

  return start <= end

def merge(prev_i, next_i):
  prev_start, prev_end = prev_i
  next_start, next_end = next_i

  return (prev_start, max(prev_end, next_end))
