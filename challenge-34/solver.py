def subset_sum(nums, target):
  return helper(0, nums, target)

def helper(acc, remaining_nums, target):
  if acc == target:
    return True
  elif acc > target:
    return False
  elif not remaining_nums:
    return False

  num = remaining_nums[0]

  # Return the backtracking with and without the next number
  return helper(acc+num, remaining_nums[1:], target) or helper(acc, remaining_nums[1:], target)
