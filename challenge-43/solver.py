#
# Time  complexity: O(n)
# Space complexity: O(1)
#
def max_subarray(nums):
  # Kadane's algorithm
  current_sum, max_sum = 0, 0

  for num in nums:
    current_sum = max(0, current_sum + num)
    max_sum     = max(max_sum, current_sum)

  return max_sum
