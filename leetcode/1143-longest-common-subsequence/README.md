# 1143. Longest Common Subsequence

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Longest_Common_Subsequence-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1068 ms |
| Memory | 30.1 MB |
| Submission Date | 2026-11-04T04:42:55.734Z |
| Platform | leetcode |

## Problem Statement

<p>Given two strings <code>text1</code> and <code>text2</code>, return <em>the length of their longest <strong>common subsequence</strong>. </em>If there is no <strong>common subsequence</strong>, return <code>0</code>.</p>

<p>A <strong>subsequence</strong> of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.</p>

<ul>
	<li>For example, <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;abcde&quot;</code>.</li>
</ul>

<p>A <strong>common subsequence</strong> of two strings is a subsequence that is common to both strings.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> text1 = &quot;abcde&quot;, text2 = &quot;ace&quot; 
<strong>Output:</strong> 3  
<strong>Explanation:</strong> The longest common subsequence is &quot;ace&quot; and its length is 3.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> text1 = &quot;abc&quot;, text2 = &quot;abc&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest common subsequence is &quot;abc&quot; and its length is 3.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> text1 = &quot;abc&quot;, text2 = &quot;def&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no such common subsequence, so the result is 0.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= text1.length, text2.length &lt;= 1000</code>
- <code>text1</code> and <code>text2</code> consist of only lowercase English characters.

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/longest-common-subsequence/)
