class Solution:
  def move_zeros(self, nums):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    k = 0

    for num in nums:
      if num != 0:
        nums[k] = num
        k += 1

    nums[k:] = [0] * (len(nums) - k)

    return nums
