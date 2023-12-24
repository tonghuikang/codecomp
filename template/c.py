#!/usr/bin/env python3
import sys

input = sys.stdin.readline  # to read input quickly


def solve(n,k,d,arr,vrr):

    # grow once and reset, repeat
    maxres = d // 2

    # reset and grow once, repeat
    res = 0
    for i,x in enumerate(arr, start=1):
        if i == x:
            res += 1
    res += (d - 1) // 2
    maxres = max(maxres, res)

    # grow multiple, reset, and grow once and reset
    for q,b in enumerate(vrr, start=1):
        res = 0
        for i in range(n):
            if i < b:
                arr[i] += 1
            if arr[i] == i+1:
                res += 1
        res += (d - q - 1) // 2
        maxres = max(maxres, res)

    return maxres


for case_num in range(int(input())):

    n,k,d = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    vrr = list(map(int,input().split()))

    res = solve(n,k,d,arr,vrr)  # include input here

    print(res)
