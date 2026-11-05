# Runtime: 65 ms
# Memory: 30.5 MB

class Solution(object):
    def longestConsecutive(self, nums):
        a = {}

        for i in nums:
            a[i] = 1

        maxi = 0

        for i in a:
            if i - 1 not in a:
                curr = i
                count = 1

                while curr + 1 in a:
                    curr += 1
                    count += 1

                maxi = max(maxi, count)

        return maxi