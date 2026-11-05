# Runtime: 22 ms
# Memory: 16.2 MB

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for word in strs:
            curr="".join(sorted(word))
            if not(curr in d):
                d[curr]=[]
            d[curr].append(word)
        return list(d.values())