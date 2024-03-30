#!/usr/bin/env python3
import sys

input = sys.stdin.readline  # to read input quickly


from collections import Counter
# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}
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


def ceiling_division(numer, denom):
    return -((-numer) // denom)


def solve_(n,len_arr,y,arr):
    # your solution here

    # auto-include vertices that are the the side
    arr.sort()
    arr_set = set(arr)

    count = 0
    for x in arr:
        if (x + 2)%n in arr_set and (x + 1)%n not in arr_set:
            count += 1

    res = count + len(arr) - 2

    # you can always add one to get two
    # but there are times you can add x to get 2*x+1
    # get those bonuses
    arr.append(arr[0] + n)

    diffs = [b-a for a,b in zip(arr, arr[1:])]
    diffs = [x for x in diffs if x > 2]
    # log(diffs)

    bonus_costs = []
    for x in diffs:
        if x%2 == 0:
            bonus_costs.append(x // 2 - 1)

    bonus_costs.sort()
    # log(res, bonus_costs)

    res += 2*y

    for x in bonus_costs:
        if x <= y:
            y -= x
            res += 1

    return min(n-2, res)


# from itertools import combinations

# def brute_force(n,len_arr,y,arr):
#     unselected = set(range(n)) - set(arr)
#     maxres = 0

#     for comb in combinations(unselected, y):
#         # log(comb)
#         brr = list(comb) + [x for x in arr]
#         brr.sort()
#         brr_set = set(brr)

#         count = 0
#         for x in brr:
#             if (x + 2)%n in brr_set and (x + 1)%n not in brr_set:
#                 count += 1

#         res = count + len(brr) - 2
#         maxres = max(maxres, res)
#     return maxres


# import random
# while True:
#     n = random.randint(4, 40)
#     x = random.randint(2, n)
#     y = random.randint(0, min(n-x, 4))
#     arr = list(range(n))
#     random.shuffle(arr)
#     arr = arr[:x]
#     arr.sort()
#     # log(arr)
#     res = solve(n,x,y,[x for x in arr])  # include input here
#     res2 = brute_force(n,x,y,[x for x in arr])
#     assert res == res2, [n,x,y,arr,res,res2]



# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,x,y = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,x,y,[x for x in arr])  # include input here
    # res = brute_force(n,x,y,[x for x in arr])
    # assert solve(n,x,y,[x for x in arr]) == brute_force(n,x,y,[x for x in arr]), [solve(n,x,y,[x for x in arr]), brute_force(n,x,y,[x for x in arr])]
    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
