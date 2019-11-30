#
# Time  complexity: O(logn)
# Space complexity: O(1)
#
def occurrences(nums, k):
  left  = binsearch(nums, k, search_min=True )
  right = binsearch(nums, k, search_min=False)

  # "k" not found on the array
  if left == -1 or right == -1:
    return 0

  return right - left + 1

def binsearch(nums, k, search_min):
  def inbounds(x):
    return 0 <= x < len(nums)

  left, right = 0, len(nums)

  while left <= right:
    middle = (left + right) // 2

    if k < nums[middle]:
      right = middle - 1
    elif k > nums[middle]:
      left = middle + 1
    else:
      if search_min:
        if inbounds(middle - 1) and nums[middle - 1] == k:
          # Proceed looking for the min on the left side
          right = middle - 1
        else:
          return middle
      else:
        if inbounds(middle + 1) and nums[middle + 1] == k:
          # Proceed looking for the max on the right side
          left = middle + 1
        else:
          return middle

  return -1
