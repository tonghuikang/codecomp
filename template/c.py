#!/usr/bin/env python3
import sys

input = sys.stdin.readline  # to read input quickly


def solve(n,k,d,arr,vrr):

    # grow once and reset, repeat
    maxres = 0

    if arr[0] == 0:
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
        if d - q <= 0:
            continue
        res += (d - q - 1) // 2
        maxres = max(maxres, res)

    return maxres


# import itertools
# def solve_ref(n,k,d,arr_original,vrr):

#     maxres = 0

#     for prod in itertools.product([0,1], repeat=d):
#         arr = [x for x in arr_original]
#         res = 0
#         for i,x in enumerate(prod):
#             if x == 0:
#                 res += sum(i == x for i,x in enumerate(arr, start=1))
#                 arr = [0 for _ in range(n)]
#             else:
#                 for q in range(vrr[i%k]):
#                     arr[q] += 1
#         maxres = max(maxres, res)

#     return maxres


# import random
# while True:
#     n = random.randint(1,2)
#     k = random.randint(1,2)
#     d = random.randint(k, 4)
#     arr = [random.randint(0,n) for _ in range(n)]
#     vrr = [random.randint(1,n) for _ in range(k)]

#     res2 = solve_ref(n,k,d,[x for x in arr],[x for x in vrr])
#     res = solve(n,k,d,[x for x in arr],[x for x in vrr])  # include input here

#     assert res == res2, (n,k,d,arr,vrr, res, res2)


for case_num in range(int(input())):

    n,k,d = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    vrr = list(map(int,input().split()))

    # res2 = solve_ref(n,k,d,arr,vrr)
    res = solve(n,k,d,arr,vrr)  # include input here

    # assert res == res2, (res, res2)

    print(res)
