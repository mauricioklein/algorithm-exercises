class Solution:
    def getRange(self, arr, target):
        left  = self.bin_search(arr, 0, len(arr)-1, target, find_min=True)
        right = self.bin_search(arr, 0, len(arr)-1, target, find_min=False)

        return [left, right]

    def bin_search(self, arr, low, high, target, find_min):
        while low <= high:
            mid = (high + low) / 2

            if arr[mid] == target: 
                if find_min and self.is_equal_previous(arr, mid):
                    high = mid - 1
                elif not find_min and self.is_equal_next(arr, mid):
                    low = mid + 1
                else:
                    return mid
            else:
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    def is_equal_previous(self, arr, index):
        return (index-1 >= 0 and arr[index-1] == arr[index])

    def is_equal_next(self, arr, index):
        return (index+1 < len(arr) and arr[index+1] == arr[index])

