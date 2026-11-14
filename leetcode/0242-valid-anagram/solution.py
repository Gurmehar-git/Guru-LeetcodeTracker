# Runtime: 17 ms
# Memory: 12.2 MB

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a={}
        b={}
        for i in s:
            a[i]=a.get(i,0)+1
        for i in t:
            b[i]=b.get(i,0)+1
        if(a==b):
            return True
        else:
            return False

        
        
