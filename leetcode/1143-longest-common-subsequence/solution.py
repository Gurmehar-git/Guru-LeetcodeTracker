# Runtime: 1068 ms
# Memory: 30.1 MB

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n=len(text1)
        m=len(text2)
        dp=[[-1]*m for _ in range(n)]
        def f(i,j):
            if(i>=n or j>=m):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            if(text1[i]==text2[j]):
                dp[i][j]=1+f(i+1,j+1)
            else:
                dp[i][j]=max(f(i+1,j),f(i,j+1))
            return dp[i][j]
        return f(0,0)