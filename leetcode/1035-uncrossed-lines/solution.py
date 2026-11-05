# Runtime: 204 ms
# Memory: 14.7 MB

class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n=len(nums1)
        m=len(nums2)
        dp=[[-1]*m for _ in range(n)]
        def f(i,j):
            if(i>=n or j>=m):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            if(nums1[i]==nums2[j]):
                dp[i][j]=1+f(i+1,j+1)
            else:
                dp[i][j]=max(f(i+1,j),f(i,j+1))
            return dp[i][j]
        return f(0,0)