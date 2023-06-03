#!/usr/bin/env python3
import sys, getpass
input = sys.stdin.readline  # to read input quickly


# ---------------------------- template ends here ----------------------------

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
    # log(arr, 0 in vals)
    return 0 in vals


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

        candidates = list(range(n))
        random.shuffle(candidates)

        for pos in candidates:
            if pos == idx:
                continue
            if arr[pos] == 0:
                continue

            val = min(arr[pos], arr[idx])
            arr[pos] -= val
            arr[idx] -= val

            if compute(arr):
                print("{}".format(pos+1), flush=True)
                break

            arr[pos] += val
            arr[idx] += val

        else:
            break

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
