class Solution:
    def lengthOfLongestSubstring(self, s):
        h = {}
        head, tail = 0, -1
        max_length = 0

        while head < len(s):
            if s[head] in h:
                tail = max(tail, h[s[head]])
            
            h[s[head]] = head
            max_length = max(max_length, head - tail)
            head += 1

        return max_length
