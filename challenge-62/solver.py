"""
  Time  complexity: O(2^min(n,k)) (where n = length of the word)
  Space complexity: O(2^min(n,k)) (for the call stack)
"""
def has_palindrome(word, k):
  return helper(word, k, 0, len(word)-1)

def helper(word, k, left, right):
  while left < right:
    if word[left] != word[right]:
      """ No more removals left: not a solution """
      if k == 0:
        return False
     
      """
      Recurse...
        - Removing the left most char  (l)
        - Removing the right most char (r)
      """
      l = helper(word, k - 1, left + 1, right    )
      r = helper(word, k - 1, left    , right - 1)

      return l or r

    left += 1
    right -= 1

  """ Found a palindrome """
  return True
