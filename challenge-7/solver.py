class Solution():
  def first_missing_positive(self, nums):
    """
      Time complexity:  O(n)
      Space complexity: O(1)
    """
    if not nums:
      return 1

    #
    # Time complexity: O(n) (rearrange elements in place, swaping each element at most once)
    #
    for i in range(len(nums)):
      while nums[i] != i+1 and 0 < nums[i] <= len(nums):
        v = nums[i]-1
        nums[i], nums[v] = nums[v], nums[i]

    #
    # Time complexity: O(n)
    #
    for i in range(len(nums)):
      if nums[i] != i+1:
        return i+1

    # No gaps in the array
    return len(nums)+1

