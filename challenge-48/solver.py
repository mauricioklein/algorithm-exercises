import bisect

#
# Brute force solution:
# For each window with "k" elements, sort the window and return the median.
#   Time  complexity: O(n*klog(k))
#   Space complexity: O(n) (for the output array)
#

#
# Optimized solution:
# Initialize the window with the "k" first elements using bisect insert to place the element while keeping the
# window sorted. For every new window, remove the oldest element and add the new one, using bisect insert.
# Return the median of each window as usual
#   Time  complexity: O(n*k)
#   Space complexity: O(n) (for the output array)

#
# Time  complexity: O(n*k) (n = number of elements in the array)
# Space complexity: O(n)   (for the output buffer)
#
def subarr_mean(arr, k):
  # Populate the buffer with the first "k" elements of the array,
  # adding them in order, to keep the array sorted: O(k)
  buffer = []
  for i in range(0, k):
    bisect.insort(buffer, arr[i])

  oldest = arr[0]
  output = [median(buffer, k)]

  for i in range(k, len(arr)):
    # Remove the oldest value: O(k)
    buffer.remove(oldest)

    # Insert the new value on the right place, in
    # order to keep the buffer sorted: O(k)
    bisect.insort(buffer, arr[i])

    # Add the median to the output array: O(1)
    output.append(median(buffer, k))

    # Update the oldest value: O(1)
    oldest = arr[i - k + 1]

  return output

#
# Time  complexity: O(1)
# Space complexity: O(1)
#
def median(subarr, k):
  """
  Return the median of the subarray based on the value ok "k"
  """
  even_k = (k % 2 == 0)

  if even_k:
    right  = k / 2
    left = right - 1

    return (subarr[left] + subarr[right]) / 2
  else:
    id = k // 2

    return subarr[id]

