#!/usr/bin/env python3
import sys
input = sys.stdin.readline

h,w,n = list(map(int,input().split()))

mrr = [[0 for _ in range(w)] for _ in range(h)]
for _ in range(n):
    x,y = list(map(int,input().split()))
    mrr[x-1][y-1] = 1

arr = [[0 for _ in range(w)] for _ in range(h)]  # right
brr = [[0 for _ in range(w)] for _ in range(h)]  # down
crr = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    count = 0
    for j in range(w):
        if mrr[i][j] == 1:
            count = 0
            continue
        count += 1
        arr[i][j] = count

for j in range(w):
    count = 0
    for i in range(h):
        if mrr[i][j] == 1:
            count = 0
            continue
        count += 1
        brr[i][j] = count

j = 0
for i in range(h):
    if mrr[i][j] == 1:
        continue
    crr[i][j] = 1

i = 0
for j in range(w):
    if mrr[i][j] == 1:
        continue
    crr[i][j] = 1

for i in range(1,h):
    for j in range(1,w):
        crr[i][j] = min(arr[i][j], brr[i][j], crr[i-1][j-1] + 1)

res = 0
for i in range(h):
    for j in range(w):
        res += crr[i][j]

print(res)
