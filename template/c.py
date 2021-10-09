#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(arr):
    # your solution here

    players = {i:0 for i in range(1, 1+len(arr))}

    for i,plays in enumerate(zip(*arr)):
        log(plays)
        p0 = plays[0::2]
        p1 = plays[1::2]

        rankings = [(x,i) for i,x in players.items()]
        rankings.sort()
        # rankings.reverse()
        log(rankings)

        x0 = rankings[0::2]
        x1 = rankings[1::2]

        # x0 = range(1,1+len(arr),2)
        # x1 = range(2,1+len(arr),2)

        for (_,y0),(_,y1) in zip(x0, x1):
            a = arr[y0-1][i]
            b = arr[y1-1][i]
            # log(a,b,y0,y1)
            if a == b:
                continue
            if a == "G" and b == "C":
                players[y0] -= 1
            if a == "C" and b == "P":
                players[y0] -= 1
            if a == "P" and b == "G":
                players[y0] -= 1

            if b == "G" and a == "C":
                players[y1] -= 1
            if b == "C" and a == "P":
                players[y1] -= 1
            if b == "P" and a == "G":
                players[y1] -= 1


    rankings = [(x,i) for i,x in players.items()]
    rankings.sort()
    # rankings.reverse()
    log(rankings)

    return [x[1] for x in rankings]


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    k,_ = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    arr = read_strings(2*k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
