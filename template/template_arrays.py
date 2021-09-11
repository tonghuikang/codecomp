#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# ------------------------ standard imports ends here ------------------------

# ---------------------- longest subsequence or subarray ----------------------


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


def longest_common_subarray(arr, brr):
    # binarysearch.com/problems/Longest-Common-Substring
    def slide_along(xrr, yrr):
        maxres = 0
        # slide yrr along xrr
        for i in range(len(xrr)):
            curres = 0  # track current length of common subarray
            for a,b in zip(xrr[i:], yrr):
                if a == b:  # increment if match
                    curres += 1
                    maxres = max(maxres, curres)
                else:  # reset if mismatch
                    curres = 0
        return maxres
    return max(slide_along(arr,brr), slide_along(brr,arr))


def longest_increasing_subsequence(nums):
    # leetcode.com/problems/longest-increasing-subsequence/discuss/667975/
    dp = [MAXINT] * (len(nums) + 1)
    for elem in nums:
        dp[bisect.bisect_left(dp, elem)] = elem
    return dp.index(MAXINT)


def max_dot_product_of_two_subsequence(A, B):
    # leetcode.com/problems/max-dot-product-of-two-subsequences/discuss/648420/
    n, m = len(A), len(B)
    dp = [[0] * (m) for i in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j] = A[i] * B[j]
            if i and j: dp[i][j] += max(dp[i - 1][j - 1], 0)
            if i: dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j: dp[i][j] = max(dp[i][j], dp[i][j - 1])
    return dp[-1][-1]


def RabinKarp(arr, window_size, modulus):
    # for longest common subarray in O(N log N), use binary search
    # run this multiple times to avoid collisions
    h, t, d = (1<<(17*window_size-17))%modulus, 0, 1<<17
    all_hashes = set()

    for i in range(window_size):
        t = (d * t + arr[i])%modulus

    all_hashes.add(t)

    for i in range(len(arr) - window_size):
        t = (d*(t-arr[i]*h) + arr[i + window_size])%modulus
        all_hashes.add(t)

    return all_hashes


# --------------------------- sliding windows ---------------------------


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


def sliding_window_median(nums, k):
    # leetcode.com/problems/sliding-window-median/discuss/262689
    def move(h1, h2):
        x, i = heapq.heappop(h1)
        heapq.heappush(h2, (-x, i))

    def get_med(h1, h2, k):
        return h2[0][0] * 1. if k & 1 else (h2[0][0]-h1[0][0]) / 2.

    small, large = [], []
    for i, x in enumerate(nums[:k]):
        heapq.heappush(small, (-x,i))
    for _ in range(k-(k>>1)):
        move(small, large)
    ans = [get_med(small, large, k)]
    for i, x in enumerate(nums[k:]):
        if x >= large[0][0]:
            heapq.heappush(large, (x, i+k))
            if nums[i] <= large[0][0]:
                move(large, small)
        else:
            heapq.heappush(small, (-x, i+k))
            if nums[i] >= large[0][0]:
                move(small, large)
        while small and small[0][1] <= i:
            heapq.heappop(small)
        while large and large[0][1] <= i:
            heapq.heappop(large)
        ans.append(get_med(small, large, k))
    return ans


def gathering_cost(xpos):
    # the cost to gather every item to each location
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


def z_function(S):
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/z_algorithm.py
    # https://cp-algorithms.com/string/z-function.html
    n = len(S)
    Z = [0] * n
    l = r = 0

    for i in range(1, n):
        z = Z[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and S[z] == S[i + z]:
                z += 1

            l, r = i, i + z

        Z[i] = z

    Z[0] = n
    return Z


def manachers(S):
    # https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/discuss/1389421/
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/suffix_array.py
    A = '@#' + '#'.join(S) + '#$'
    Z = [0] * len(A)
    center = right = 0
    for i in range(1, len(A) - 1):
        if i < right:
            Z[i] = min(right - i, Z[2 * center - i])
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
            Z[i] += 1
        if i + Z[i] > right:
            center, right = i, i + Z[i]
    return Z[2:-2:2]
