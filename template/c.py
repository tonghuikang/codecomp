#!/usr/bin/env python3
import sys
input = sys.stdin.readline  # to read input quickly


def query(pos):
    print("{}".format(pos), flush=True)
    response = int(input())
    return response


for case_num in range(int(input())):
    # read line as an integer
    n = int(input())
    arr = list(map(int,input().split()))

    arrset = set(arr)
    cur = 0
    while cur in arrset:
        cur += 1

    while True:
        cur = query(cur)
        if cur == -1:
            break
        if cur == -2:
            assert False
            break

sys.exit()

