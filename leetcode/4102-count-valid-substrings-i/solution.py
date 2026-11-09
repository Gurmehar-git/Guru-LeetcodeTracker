# Runtime: 260 ms
# Memory: 16 MB

class Solution(object):
    def countValidSubstrings(self, s):
        c = 0
        last = -1
        for end in range(len(s)):
            if end >= 2 and s[end - 2:end + 1] == "abc":
                last = end - 2
            c += end - last
        return c
