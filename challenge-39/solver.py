#
# Time  complexity: O(n^2)
# Space complexity: O(1)
#
def remove_exponential(nums):
  i, j = 0, 0

  while i < len(nums):
    sum = nums[i]

    j = i + 1
    while j < len(nums):
      sum += nums[j]

      if sum == 0:
        del nums[i:j+1]
        i = i - 1
        break

      j += 1
    i += 1

  return nums

#
# Time  complexity: O(n)
# Space complexity: O(n) (for the hash)
#
#
def remove_linear(nums):
  def in_hash(num):
    return num in saw and saw[num] <= min_id_hash

  i = min_id_hash = sum = 0
  saw = { 0: -1 }

  while i < len(nums):
    sum += nums[i]

    if in_hash(sum):
      # Found a zero sum:
      # Delete the range and set "i" to the next
      # value after the deleted window
      start, end = saw[sum]+1, i+1
      del nums[start:end]

      i = min_id_hash = saw[sum]
    else:
      # No zero sum found:
      # mark the accumulated sum in hash
      saw[sum] = i
      min_id_hash = max(min_id_hash, i)

    i += 1

  return nums
