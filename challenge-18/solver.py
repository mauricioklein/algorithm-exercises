class Solution:
    def longestPalindrome(self, s):
        longest = ''

        for i in range(len(s)):
            l1 = self.expand(s,i,i)
            l2 = self.expand(s,i,i+1)

            longest = max(longest, l1, l2, key=len)

        return longest

    def expand(self, s, left, right):
        while left > -1 and right < len(s):
            if s[left] != s[right]:
                break

            left -= 1
            right += 1

        return s[left+1:right]
