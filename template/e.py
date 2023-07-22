#!/usr/bin/env python3
import sys
input = sys.stdin.readline

h,w,n = list(map(int,input().split()))
mrr = set()
for _ in range(n):
    x,y = list(map(int,input().split()))
    mrr.add((x-1, y-1))

arr = [[0 for _ in range(w)] for _ in range(h)]  # right
brr = [[0 for _ in range(w)] for _ in range(h)]  # down
crr = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    count = 0
    for j in range(w):
        if (i,j) in mrr:
            count = 0
            continue
        count += 1
        arr[i][j] = count

for j in range(w):
    count = 0
    for i in range(h):
        if (i,j) in mrr:
            count = 0
            continue
        count += 1
        brr[i][j] = count

for i in range(h):
    if (i,0) in mrr:
        continue
    crr[i][0] = 1

for j in range(w):
    if (0,j) in mrr:
        continue
    crr[0][j] = 1

for i in range(1,h):
    for j in range(1,w):
        crr[i][j] = min(arr[i][j], brr[i][j], crr[i-1][j-1] + 1)

res = 0
for i in range(h):
    for j in range(w):
        res += crr[i][j]

print(res)
