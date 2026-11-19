# 188. Best Time to Buy and Sell Stock IV

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 284 ms |
| Memory | 19.6 MB |
| Submission Date | 2026-11-19T03:54:48.969Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day, and an integer <code>k</code>.</p>

<p>Find the maximum profit you can achieve. You may complete at most <code>k</code> transactions: i.e. you may buy at most <code>k</code> times and sell at most <code>k</code> times.</p>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> k = 2, prices = [2,4,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> k = 2, prices = [3,2,6,5,0,3]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= k &lt;= 100</code>
- <code>1 &lt;= prices.length &lt;= 1000</code>
- <code>0 &lt;= prices[i] &lt;= 1000</code>

## Solution

```py
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[[-1]*(k+1) for _ in range(2)] for _ in range(n)]
        def f(i, buy, cap):
            if i == n or cap == 0:
                return 0
            if dp[i][buy][cap] != -1:
                return dp[i][buy][cap]
            if buy == 1:
                take = -prices[i] + f(i+1, 0, cap)
                nottake = f(i+1, 1, cap)
                profit = max(take, nottake)
            else:
                sell = prices[i] + f(i+1, 1, cap-1)
                notsell = f(i+1, 0, cap)
                profit = max(sell, notsell)
            dp[i][buy][cap] = profit
            return profit
        return f(0,1,k)
```

[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
