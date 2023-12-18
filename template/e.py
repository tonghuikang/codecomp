#!/usr/bin/env python3
import sys
import random

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
# abc = "abcdefghijklmnopqrstuvwxyz"
# abc_map = {c:i for i,c in enumerate(abc)}
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass

    OFFLINE_TEST = getpass.getuser() == "htong"


def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x - 1 for x in arr]


def minus_one_matrix(mrr):
    return [[x - 1 for x in row] for row in mrr]


# ---------------------------- template ends here ----------------------------


def solve_(n,m,mrr,arr,brr):

    mrr_original = [[x for x in row] for row in mrr]
    # just greedy

    if sum(arr) != sum(brr):
        return -1

    if 0 in arr and n in brr:
        return -1

    if 0 in brr and m in arr:
        return -1

    # res = 0

    # flag = True

    # while flag:
    #     flag = False

    #     # remove zero rows
    #     n = len(mrr)
    #     m = len(mrr[0])

    #     for i,x in enumerate(arr):
    #         if x == 0:
    #             flag = True
    #             for j in range(m):
    #                 if mrr[i][j] == 1:
    #                     res += 1

    #     mrr = [[x for j,x in enumerate(row)] for i,row in enumerate(mrr) if arr[i] > 0]
    #     arr = [x for x in arr if x > 0]

    #     if mrr == []:
    #         return res

    #     # remove zero columns
    #     n = len(mrr)
    #     m = len(mrr[0])

    #     for j,x in enumerate(brr):
    #         if x == 0:
    #             flag = True
    #             for i in range(n):
    #                 if mrr[i][j] == 1:
    #                     res += 1

    #     mrr = [[x for j,x in enumerate(row) if brr[j] > 0] for i,row in enumerate(mrr)]
    #     brr = [x for x in brr if x > 0]

    #     if mrr == []:
    #         return res

    #     log(arr)
    #     log(brr)
    #     log()

    #     for row in mrr:
    #         log(row)
    #     log()

    #     log()
    #     log("--")
    #     log()

    #     # remove max rows
    #     n = len(mrr)
    #     m = len(mrr[0])

    #     for i,x in enumerate(arr):
    #         if x == m:
    #             flag = True
    #             for j in range(m):
    #                 brr[j] -= 1
    #                 if mrr[i][j] == 0:
    #                     res += 1

    #     mrr = [[x for j,x in enumerate(row)] for i,row in enumerate(mrr) if arr[i] < m]
    #     arr = [x for x in arr if x < m]

    #     if mrr == []:
    #         return res

    #     # remove max columns
    #     n = len(mrr)
    #     m = len(mrr[0])

    #     for j,x in enumerate(brr):
    #         if x == n:
    #             flag = True
    #             for i in range(n):
    #                 arr[i] -= 1
    #                 if mrr[i][j] == 0:
    #                     res += 1

    #     mrr = [[x for j,x in enumerate(row) if brr[j] < n] for i,row in enumerate(mrr)]
    #     brr = [x for x in brr if x < n]

    #     if mrr == []:
    #         return res

    #     log(arr)
    #     log(brr)
    #     log()

    #     for row in mrr:
    #         log(row)
    #     log()

    #     log()
    #     log("--")
    #     log()

    #     if len(arr) == len(brr) == 0:
    #         return res
    
    # assert sum(arr) == sum(brr), (arr, brr)

    carr = [0 for _ in range(n)]
    cbrr = [0 for _ in range(m)]

    for i,row in enumerate(mrr):
        for j,cell in enumerate(row):
            carr[i] += cell
            cbrr[j] += cell

    darr = [b-a for a,b in zip(arr, carr)]
    dbrr = [b-a for a,b in zip(brr, cbrr)]

    log(darr)
    log(dbrr)
    log()

    # visited = set()
    xrr = list(range(n))
    yrr = list(range(m))

    cnt = 0
    flag = True
    while flag:
        cnt += 1
        if cnt > 2_000:
            return -1

        if all(x == 0 for x in darr) and all(x == 0 for x in dbrr):
            break

        random.shuffle(xrr)
        random.shuffle(yrr)
        flag = False
        # for row in mrr:
        #     log(row)
        # log()

        for i in xrr:
            for j in yrr:
                if (arr[i] == 0 or brr[j] == 0) and mrr[i][j] == 1:
                    darr[i] -= 1
                    dbrr[j] -= 1
                    mrr[i][j] = 0
                    flag = True
                if flag:
                    continue

                if (arr[i] == m or brr[j] == n) and mrr[i][j] == 0:
                    darr[i] += 1
                    dbrr[j] += 1
                    mrr[i][j] = 1
                    flag = True
                if flag:
                    continue
            if flag:
                continue
        if flag:
            continue

        for i in xrr:
            for j in yrr:
                if darr[i] > 0 and dbrr[j] > 0 and mrr[i][j] == 1:
                    darr[i] -= 1
                    dbrr[j] -= 1
                    mrr[i][j] = 0
                    flag = True
                if flag:
                    continue ##

                if darr[i] < 0 and dbrr[j] < 0 and mrr[i][j] == 0:
                    darr[i] += 1
                    dbrr[j] += 1
                    mrr[i][j] = 1
                    flag = True
                if flag:
                    continue
            if flag:
                continue
        if flag:
            continue

        for i in xrr:
            for j in yrr:
                if (darr[i] > 0 or dbrr[j] > 0) and mrr[i][j] == 1:
                    darr[i] -= 1
                    dbrr[j] -= 1
                    mrr[i][j] = 0
                    flag = True
                if flag:
                    continue

                if (darr[i] < 0 or dbrr[j] < 0) and mrr[i][j] == 0:
                    darr[i] += 1
                    dbrr[j] += 1
                    mrr[i][j] = 1
                    flag = True
                if flag:
                    continue
            if flag:
                continue
        if flag:
            continue


    # log("-")
    # log()

    # for row in mrr:
    #     log(row)
    # log()

    # log(darr)
    # log(dbrr)
    # log()

    assert all(x == 0 for x in darr)
    assert all(x == 0 for x in dbrr)

    res = 0
    for i in range(n):
        for j in range(m):
            res += abs(mrr_original[i][j] - mrr[i][j]) 

    return res


# while True:
#     import random
#     n = random.randint(1,4)
#     m = random.randint(1,4)
#     mrr = [[random.randint(0,1) for _ in range(m)] for _ in range(n)]
#     arr = [random.randint(0, m) for _ in range(n)]
#     brr = [random.randint(0, n) for _ in range(m)]
#     log(n, m)
#     val = solve(n,m,[[x for x in row] for row in mrr],[x for x in arr],[x for x in brr])
#     for _ in range(3):
#         val2 = solve(n,m,[[x for x in row] for row in mrr],[x for x in arr],[x for x in brr])
#         assert val == val2, (val, val2, n, m, mrr, arr, brr)

for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))

    minres = n * m
    for i in range(5):
        res = solve(n,m,[[x for x in row] for row in mrr],[x for x in arr],[x for x in brr])  # include input here
        minres = min(minres, res)

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(minres)
