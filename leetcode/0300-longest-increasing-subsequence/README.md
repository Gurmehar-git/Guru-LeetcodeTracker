# 300. Longest Increasing Subsequence

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Longest_Increasing_Subsequence-blue) ![Language](https://img.shields.io/badge/Language-java-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 415 ms |
| Memory | 236.8 MB |
| Submission Date | 2026-11-16T04:34:15.457Z |
| Platform | leetcode |

## Problem Statement

<p>Given an integer array <code>nums</code>, return <em>the length of the longest <strong>strictly increasing </strong></em><span data-keyword="subsequence-array"><em><strong>subsequence</strong></em></span>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [10,9,2,5,3,7,101,18]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [0,1,0,3,2,3]
<strong>Output:</strong> 4
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> nums = [7,7,7,7,7,7,7]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 2500</code>
- <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>

## Solution

```java
import java.util.Arrays;
class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[][] dp = new int[n][n + 1];
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }
        return f(0, -1, nums, dp);
    }
    private int f(int i, int prev, int[] nums, int[][] dp) {
        int n = nums.length;
        if (i >= n) {
            return 0;
        }
        if (dp[i][prev + 1] != -1) {
            return dp[i][prev + 1];
        }
        int take = 0;
        if (prev == -1 || nums[i] > nums[prev]) {
            take = 1 + f(i + 1, i, nums, dp);
        }
        int nottake = f(i + 1, prev, nums, dp);
        dp[i][prev + 1] = Math.max(take, nottake);
        return dp[i][prev + 1];
    }
}

```

[View on LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)
