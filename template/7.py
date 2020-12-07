import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_(arr):
    # your solution here
    main = [x.split("contain")[0][:-6] for x in arr]
    supp = [x.split("contain")[1][:-1] for x in arr]
    supp = [x.replace("bags", "").replace("bag", "") for x in supp]
    supp = [[y.strip() for y in x.split(",")] for x in supp]
    supp = [[y.split() for y in x] for x in supp]

    d = defaultdict(list)
    d2 = defaultdict(list)
    for m,s in zip(main, supp):
        for x in s:
            if x[0] == "no":
                continue
            d[m].append((int(x[0]), x[1]+" "+x[2]))
            d2[x[1]+" "+x[2]].append(m)
    log(main)
    log(supp)
    log(d)
    log(d2)

    visited = set()
    stack = ["shiny gold"]
    res = 0
    while stack:
        cur = stack.pop()
        for nex in d2[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            res += 1
            stack.append(nex)

    import functools
    @functools.lru_cache(maxsize=None)
    def bags(color):
        if color not in d:
            return 1
        res = 1
        for count, nex in d[color]:
            res += count*bags(nex)
        return res

    res = bags("shiny gold")

    return res-1


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

arr = []
while True:  # no loop over test case
# for case_num in range(int(input())):

    # read line as a string
    strr = input().strip()
    if strr == "EXIT":
        break
    arr.append(strr)

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

res = solve(arr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list