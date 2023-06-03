#!/usr/bin/env python3
import sys, getpass
input = sys.stdin.readline  # to read input quickly


# ---------------------------- template ends here ----------------------------

OFFLINE_TEST = getpass.getuser() == "htong"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def compute(arr):
    arr = sorted(arr)
    vals = set([0])
    suffix_size = sum(arr)
    for x in arr:
        suffix_size -= x
        new_vals = set()
        for y in vals:
            if x+y <= suffix_size:
                new_vals.add(x+y)
            if x+y >= -suffix_size:
                new_vals.add(x-y)
        vals = new_vals
    return 0 in vals


from collections import Counter
def can_partition(arr):
    total_sum = sum(arr)
    
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    n = len(arr)

    dp = [False] * (target_sum + 1)
    dp[0] = True

    for num in arr:
        for j in range(target_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target_sum]


def find_subset(arr):
    if not can_partition(arr):
        return None

    total_sum = sum(arr)
    target_sum = total_sum // 2
    n = len(arr)

    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]

    subset = []
    i, j = n, target_sum
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            subset.append(arr[i - 1])
            j -= arr[i - 1]
        i -= 1

    left = subset

    c = Counter(left)
    right = []
    for x in arr:
        log(x, c[x])
        if c[x] > 0:
            c[x] -= 1
            continue
        right.append(x)

    log(sum(left), sum(right), sum(arr))
    assert sum(left) == sum(right)
    assert sum(left) + sum(right) == sum(arr)
    assert sorted(left + right) == sorted(arr)
    return left, right


def query(pos):
    print("{}".format(pos+1), flush=True)
    response = int(input())
    return response



# -----------------------------------------------------------------------------

import random

# read line as an integer
n = int(input())
arr = list(map(int,input().split()))

if compute(arr):
    print("Second", flush=True)

    while True:
        log(arr)
        response = int(input())
        if response == 0:
            sys.exit()
        idx = response - 1
        assert arr[idx] != 0

        brr = [x for x in arr if x > 0]
        left, right = find_subset(brr)
        if arr[idx] in left:
            candidate = right[-1]
        else:
            candidate = left[-1]

        # log(left, right)

        for pos in range(n):
            if pos == idx:
                continue
            if candidate == arr[pos]:
                break
        else:
            assert False

        # log(arr[idx], arr[pos], idx, pos, candidate)

        val = min(arr[pos], arr[idx])
        arr[pos] -= val
        arr[idx] -= val
        print("{}".format(pos+1), flush=True)
else:
    print("First", flush=True)
    while True:
        pos = arr.index(max(arr))
        idx = query(pos)
        if idx == 0:
            sys.exit()
        idx -= 1

        val = min(arr[pos], arr[idx])
        arr[pos] -= val
        arr[idx] -= val
