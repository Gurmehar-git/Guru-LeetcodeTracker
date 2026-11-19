# 123. Best Time to Buy and Sell Stock III

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 3732 ms |
| Memory | 168.6 MB |
| Submission Date | 2026-11-19T03:50:08.715Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>Find the maximum profit you can achieve. You may complete <strong>at most two transactions</strong>.</p>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> prices = [3,3,5,0,0,3,1,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code>
- <code>0 &lt;= prices[i] &lt;= 10<sup>5</sup></code>

## Solution

```py
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[[-1]*3 for _ in range(2)] for _ in range(n)]

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

        return f(0, 1, 2)
```

[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
