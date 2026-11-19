# 121. Best Time to Buy and Sell Stock

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 136 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-11-19T03:45:49.742Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code>
- <code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code>

## Solution

```py
class Solution(object):
    def maxProfit(self, prices):
        mini = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - mini)
            mini = min(mini, prices[i])

        return profit
        
```

[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
