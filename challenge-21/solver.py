class Solution():
  def sortNumsV1(self, arr):
    """
      Time complexity:  O(n)
      Space complexity: O(n) (result is a new sorted array)
    """
    occurrences = [0, 0, 0] # ["occurrences #1", "occurences #2", "occurrences #3"]

    for num in arr:
      dic[num-1] += 1

    return [1] * dic[0] + [2] * dic[1] + [3] * dic[2]

  def sortNumsV2(self, arr):
    """
      Time complexity:  O(n)
      Space complexity: O(1) (sort is performed in place)
    """
    left, right = 0, len(arr) - 1
    index = 0

    while index <= right:
      if arr[index] == 1:
        arr[left], arr[index] = arr[index], arr[left]
        left += 1
        index += 1
      elif arr[index] == 2:
        index += 1
      elif arr[index] == 3:
        arr[right], arr[index] = arr[index], arr[right]
        right -= 1

    return arr
