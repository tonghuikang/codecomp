#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# ------------------------ standard imports ends here ------------------------


def longest_common_subsequence(arr, brr):
    # leetcode.com/problems/longest-common-subsequence/discuss/351689/
    m, n = map(len, (arr, brr))
    if m < n:
        return longest_common_subsequence(brr, arr)
    dp = [0] * (n + 1)
    for c in arr:
        prevRow, prevRowPrevCol = 0, 0
        for j, d in enumerate(brr):
            prevRow, prevRowPrevCol = dp[j + 1], prevRow
            dp[j + 1] = prevRowPrevCol + 1 if c == d else max(dp[j], prevRow)
    return dp[-1]


# add longest common subarray


def maxDotProduct(self, A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m) for i in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j] = A[i] * B[j]
            if i and j: dp[i][j] += max(dp[i - 1][j - 1], 0)
            if i: dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j: dp[i][j] = max(dp[i][j], dp[i][j - 1])
    return dp[-1][-1]


def longest_increasing_subsequence(nums):
    # leetcode.com/problems/longest-increasing-subsequence/discuss/667975/
    dp = [MAXINT] * (len(nums) + 1)
    for elem in nums:
        dp[bisect.bisect_left(dp, elem)] = elem  
    return dp.index(MAXINT)


def sliding_window_sum(nums, k):
    out = [sum(nums[:k])]
    for i in range(k, len(nums)):
        out.append(out[-1] - nums[i-k] + nums[i])
    return out


def sliding_window_maximum(nums, k):
    # leetcode.com/problems/sliding-window-maximum/discuss/65901
    deq, n, ans = deque([0]), len(nums), []
    for i in range (n):
        while deq and deq[0] <= i - k:
            deq.popleft()
        while deq and nums[i] >= nums[deq[-1]] :
            deq.pop()
        deq.append(i)
        ans.append(nums[deq[0]])
    return ans[k-1:]


# leetcode.com/problems/sliding-window-median/


def gathering_cost(xpos):
    # the cost to gather every item to a each location
    xpos = sorted(xpos)
    n = len(xpos)
    left_cost = 0
    right_cost = sum([x-xpos[0] for x in xpos])
    cost_arr = [right_cost]

    for i,(prev,nex) in enumerate(zip(xpos,xpos[1:])):
        left_cost += (i+1)*(nex - prev)
        right_cost -= (n-i-1)*(nex - prev)
        cost_arr.append(left_cost + right_cost)
    return cost_arr