# Runtime: 1 ms
# Memory: 13.2 MB

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=sum(nums)
        n=len(nums)
        total=n*(n+1)//2
        return total-s