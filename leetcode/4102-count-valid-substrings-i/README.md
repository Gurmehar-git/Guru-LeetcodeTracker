# 4102. Count Valid Substrings I

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 279 ms |
| Memory | 16.1 MB |
| Submission Date | 2026-11-08T19:09:05.256Z |
| Platform | leetcode |

## Problem Statement

<p>You are given a string <code>s</code> consisting only of the characters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</p>

<p>A string is called <strong>valid</strong> if it does not contain <code>&quot;abc&quot;</code> as a <strong>substring</strong>.</p>

<p>Return the number of <strong>valid substrings</strong> in <code>s</code>. Substrings with different starting or ending indices are counted separately.</p>

<p>A <strong>substring</strong> is a contiguous <b>non-empty</b> sequence of characters within a string.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abac&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>The following substrings don&#39;t contain <code>&quot;abc&quot;</code>​​​​​​​ as a substring:</p>

<ul>
	<li><code>s[0..0] = &quot;a&quot;</code></li>
	<li><code>s[0..1] = &quot;ab&quot;</code></li>
	<li><code>s[0..2] = &quot;aba&quot;</code></li>
	<li><code>s[0..3] = &quot;abac&quot;</code>​​​​​​​</li>
	<li><code>s[1..1] = &quot;b&quot;</code></li>
	<li><code>s[1..2] = &quot;ba&quot;</code></li>
	<li><code>s[1..3] = &quot;bac&quot;</code></li>
	<li><code>s[2..2] = &quot;a&quot;</code></li>
	<li><code>s[2..3] = &quot;ac&quot;</code></li>
	<li><code>s[3..3] = &quot;c&quot;</code></li>
</ul>

<p>Thus, the answer is 10.</p>
</div>

<p>
```

**Example 2:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The following substrings don&#39;t contain <code>&quot;abc&quot;</code>​​​​​​​ as a substring:</p>

<ul>
	<li><code>s[0..0] = &quot;a&quot;</code></li>
	<li><code>s[0..1] = &quot;ab&quot;</code></li>
	<li><code>s[1..1] = &quot;b&quot;</code></li>
	<li><code>s[1..2] = &quot;bc&quot;</code></li>
	<li><code>s[2..2] = &quot;c&quot;</code>​​​​​​​</li>
</ul>

<p>Thus, the answer is 5.</p>
</div>

<p>
```

**Example 3:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;ac&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>All substrings in <code>s</code> don&#39;t contain <code>&quot;abc&quot;</code> as a substring​​​​​​​. Thus, the answer is 3.</p>
</div>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>​​​​​​​
- <code>s</code> only consists of <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code> characters.

## Solution

```py
class Solution(object):
    def countValidSubstrings(self, s):
        c = 0
        last = -1
        for end in range(len(s)):
            if end >= 2 and s[end - 2:end + 1] == "abc":
                last = end - 2
            c += end - last
        return c

```

[View on LeetCode](https://leetcode.com/problems/count-valid-substrings-i/)
