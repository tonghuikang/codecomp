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
def distribute_to_equal_subset_sum(arr):
    total_sum = sum(arr)

    if total_sum % 2 != 0:
        return None

    target_sum = total_sum // 2
    n = len(arr)

    # Initialize the dynamic programming table
    dp = [False] * (target_sum + 1)
    dp[0] = True

    for i in range(n):
        for j in range(target_sum, arr[i] - 1, -1):
            if not dp[j]:
                dp[j] = dp[j - arr[i]]

    if not dp[target_sum]:
        return None

    # Backtrack to find the subset
    subset = []
    j = target_sum
    for i in range(n - 1, -1, -1):
        if j >= arr[i] and dp[j - arr[i]]:
            subset.append(arr[i])
            j -= arr[i]

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

    left = distribute_to_equal_subset_sum
    while True:
        log(arr)
        response = int(input())
        if response == 0:
            sys.exit()
        idx = response - 1
        assert arr[idx] != 0

        brr = [x for x in arr if x > 0]
        left, right = distribute_to_equal_subset_sum(brr)
        if arr[idx] in left:
            candidate = right[-1]
        else:
            candidate = left[-1]

        for pos in range(n):
            if candidate != arr[pos]:
                continue
            if pos == idx:
                continue
            break
        else:
            assert False

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
