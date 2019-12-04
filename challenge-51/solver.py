#
# Time  complexity: O(2^n) (where "n" is the number of letters in the string)
# Space complexity: O(2^n) (number of branches in the recursion tree)
#
def subsequences(str):
  return helper("", str)

def helper(acc, remaining):
  if not remaining:
    return [acc]

  with_letter    = helper(acc + remaining[0], remaining[1:])
  without_letter = helper(acc               , remaining[1:])

  return with_letter + without_letter
