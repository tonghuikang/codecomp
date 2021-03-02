#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
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

# ---------------------------- template ends here ----------------------------


def solve_(mrr):
    # your solution here

    # mrr = [[i]+row for i,row in enumerate(mrr, start=1)]
    # mrr = [list(range(len(mrr[0])))] + mrr

    salaries = {}
    common_supervisor = defaultdict(Counter)
    heap = []
    for i,row in enumerate(mrr):
        for j,salary in enumerate(row):
            if i == j:
                salaries[i] = salary
                continue
            common_supervisor[i][j] = salary
            common_supervisor[j][i] = salary
            heapq.heappush(heap, (salary,i,j))
            # heapq.heappush(heap, (salary,j,i))
    eliminated = set()
    supervisor_tree = {}
    idx = len(mrr)

    while heap:
        salary,i,j = heapq.heappop(heap)
        if i in eliminated or j in eliminated:
            continue
        supervisor_tree[i] = idx
        supervisor_tree[j] = idx
        salaries[idx] = salary

        paired = set()
        for y in list(common_supervisor.keys()):
            if y == i or y == j:
                continue
            for x in list(common_supervisor.keys()):
                if i == x or x == y or x in eliminated:
                    continue
                supervisor_salary = common_supervisor[i][x]
                if supervisor_salary != common_supervisor[y][x]:
                    log(i,j,x,y)
                    break
            else:
                paired.add(y)
        # log(i,j,paired)

        for x in list(common_supervisor.keys()):
            if x == i or x == j or x in eliminated:
                continue
            supervisor_salary = common_supervisor[i][x]
            assert supervisor_salary == common_supervisor[j][x]
            common_supervisor[idx][x] = supervisor_salary
            common_supervisor[x][idx] = supervisor_salary
            heapq.heappush(heap, (supervisor_salary,idx,x))
            # heapq.heappush(heap, (supervisor_salary,x,idx))
        del common_supervisor[i]
        del common_supervisor[j]
        eliminated.add(i)
        eliminated.add(j)
        for x in list(common_supervisor.keys()):
            if i in common_supervisor[x]:
                del common_supervisor[x][i]
            if j in common_supervisor[x]:
                del common_supervisor[x][j]

        for nex in paired:
            del common_supervisor[nex]
            eliminated.add(nex)
            supervisor_tree[nex] = idx
            for x in list(common_supervisor.keys()):
                if nex in common_supervisor[x]:
                    del common_supervisor[x][nex]
                if nex in common_supervisor[x]:
                    del common_supervisor[x][nex]

        idx += 1

    # log(supervisor_tree)
    # log(salaries)


    print(len(salaries))

    salaries_arr = list(v for k,v in sorted(salaries.items()))
    print(*salaries_arr)

    boss = salaries_arr.index(max(salaries_arr)) + 1
    print(boss)

    for k,v in supervisor_tree.items():
        print(k+1, v+1)

    return ""


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)