#
# Time complexity : O(n*klogk) 
#   (where n = number of anagrams, k = length of the largest anagram) 
#   (klogk because we sort every anagram once)
# Space complexity: O(n)
#
def group_anagrams(anagrams):
  groups = {}

  for word in anagrams:
    sorted_word = ''.join(sorted(word))

    if sorted_word in groups:
      groups[sorted_word].append(word)
    else:
      groups[sorted_word] = [word]

  return [g for g in groups.values()]
