import random

def k_largest(nums, k):
  N = len(nums)

  k_index = N - k
  quick_select(nums, k_index, 0, N-1)

  return nums[k_index]

def quick_select(nums, k, left, right):
  if left == right:
    return

  wall, pivot = left, ((right + left) // 2)

  # Move pivot to the end of the list
  swap(nums, right, pivot)
  pivot = right

  for i in range(left, right):
    if nums[i] < nums[pivot]:
      swap(nums, i, wall)
      wall += 1

  # Put pivot in the right place
  swap(nums, wall, pivot)
  pivot = wall

  if k < pivot:
    quick_select(nums, k, left, pivot - 1)
  elif k > pivot:
    quick_select(nums, k, pivot + 1, right)

def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]
