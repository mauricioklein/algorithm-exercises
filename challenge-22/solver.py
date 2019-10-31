class Solution():
  def two_sum(self, nums, target):
    """
      Time complexity:  O(n)
      Space complexity: O(n) (because of the auxiliar set to store the previous values)
    """
    previous_nums = set()

    for num in nums:
      complement = target - num

      if complement in previous_nums:
        return True

      previous_nums.add(num)

    return False
