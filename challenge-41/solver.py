#
# Time  complexity: O(n*log(n)) (for the sorting)
# Space complexity: O(1)
#
def max_sequence_length(nums):
  nums.sort()

  max_seq, cur_seq = 0, 0
  prev_num = None

  for num in nums:
    if prev_num == None or prev_num + 1 == num:
      cur_seq += 1
    else:
      max_seq = max(max_seq, cur_seq)
      cur_seq = 1

    prev_num = num

  # Remaining
  max_seq = max(max_seq, cur_seq)
  
  return max_seq
