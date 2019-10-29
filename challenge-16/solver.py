class Solution:
    def addTwoNumbers(self, l1, l2):
        minSize = min(len(l1), len(l2))
        out = []
        carry = 0

        for i in range(minSize):
            sum = l1[i] + l2[i] + carry

            if sum > 9:
                out.append(sum-10)
                carry = 1
            else:
                out.append(sum)
                carry = 0

        if len(l1) > minSize:
            for i in range(minSize, len(l1)):
                out.append(l1[i])

        if len(l2) > minSize:
            for i in range(minSize, len(l2)):
                out.append(l2[i])

        return out
