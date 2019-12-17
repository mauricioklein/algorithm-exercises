#
# Time complexity : O(n)       (every elements is swapped at most once)
# Space complexity: O(1000000) (constant one million, for the extended array)
#
def first_thousand_missing(nums):
  # Extend the array to length 1M, filling with "None"
  diff = 1000000 - len(nums)
  nums.extend([None for _ in range(diff)])

  # Put the elements in the right position (i.e. nums[i] = i+1)
  # If find a "None", skip it)
  for i in range(len(nums)):
    while nums[i] != None and nums[i] != i+1:
      num = nums[i]
      nums[i], nums[num - 1] = nums[num - 1], nums[i]

  # Iterate over the nums and, when find a "None", means
  # the element at the position is missing
  missing = []
  for i in range(len(nums)):
    if nums[i] == None:
      missing.append(i+1)

  return missing
