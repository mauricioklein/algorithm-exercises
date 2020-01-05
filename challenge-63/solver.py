"""
  Time  complexity: O(n^2)
  Space complexity: O(n^2) (for the recursion tree)
"""
def jumps_to_end(nums):
  return helper(nums, 0, 0)

def helper(nums, acc_jumps, index):
  N = len(nums)

  if index == N - 1:
    return acc_jumps

  if index >= N:
    return float('inf')

  best = float('inf')

  for i in range(1, nums[index] + 1):
    best = min(best, helper(nums, acc_jumps + 1, index + i))

  return best
