# 16. 3Sum Closest

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 467 ms |
| Memory | 12 MB |
| Submission Date | 2026-11-07T09:50:00.560Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>target</code>.</p>

<p>Find three integers at <strong>distinct indices</strong> in <code>nums</code> such that the sum is <strong>closest</strong> to <code>target</code>.</p>

<p>Return the sum of the three integers.</p>

<p>You may assume that each input would have <strong>exactly</strong> one solution.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [-1,2,1,-4], target = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [0,0,0], target = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>3 &lt;= nums.length &lt;= 500</code>
- <code>-1000 &lt;= nums[i] &lt;= 1000</code>
- <code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code>

## Solution

```py
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(total-target) < abs(closest-target):
                    closest = total
                if total == target:
                    return total
                elif total < target:
                    j += 1
                else:
                    k -= 1
        return closest

```

[View on LeetCode](https://leetcode.com/problems/3sum-closest/)
