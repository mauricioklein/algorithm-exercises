def split(arr):
  half = len(arr) // 2
  return [arr[:half], arr[half:]]

def merge_sorted_splits(left, right):
  left_index = right_index = 0
  merged_array = []

  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      merged_array.append(left[left_index])
      left_index += 1
    else: 
      merged_array.append(right[right_index])
      right_index += 1

  merged_array += left[left_index:]
  merged_array += right[right_index:]

  return merged_array

def merge_sort(arr):
  if len(arr) < 2:
    return arr

  left, right = split(arr)

  return merge_sorted_splits(merge_sort(left), merge_sort(right))
