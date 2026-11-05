# 128. Longest Consecutive Sequence

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Union--Find-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 65 ms |
| Memory | 30.5 MB |
| Submission Date | 2026-11-05T10:15:35.598Z |
| Platform | leetcode |

## Problem Statement

<p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,0,1,2]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code>
- <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)
