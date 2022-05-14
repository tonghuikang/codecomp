#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "htong"
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


def solve_(nrr, mrr, n):
    # your solution here

    bx,by = mrr[0][0], mrr[0][1]        
    mrr = mrr[1:]

    # for i,x in enumerate(mrr):
    #     print(mrr)

    start_state = ((1,)*n, (1,)*n, )
    states = set([start_state])

    prev = {}
    actions = {}
        
    for _ in range(n):
        # log(states)
        new_states = set()
        for state in states:

            children_remaining, sweets_remaining = state

            children_position_considered = set()
            children_remaining = list(children_remaining)

            for child, is_child_remaining in enumerate(children_remaining):
                if not is_child_remaining:
                    continue

                cx,cy = nrr[child]

                if (cx,cy) in children_position_considered:
                    continue
                children_position_considered.add((cx,cy))

                closest_dist = (cx-bx)**2 + (cy-by)**2

                for sweet, is_sweet_remaining in enumerate(sweets_remaining):
                    if not is_sweet_remaining:
                        continue
                    sx,sy = mrr[sweet]
                    dist = (cx-sx)**2 + (cy-sy)**2
                    closest_dist = min(closest_dist, dist)

                removable_sweets = set()
                sweet_position_considered = set()

                for sweet, is_sweet_remaining in enumerate(sweets_remaining):
                    if not is_sweet_remaining:
                        continue
                    sx,sy = mrr[sweet]

                    if (sx,sy) in sweet_position_considered:
                        continue
                    sweet_position_considered.add((sx,sy))

                    dist = (cx-sx)**2 + (cy-sy)**2
                    if dist == closest_dist:
                        removable_sweets.add(sweet)

                if not removable_sweets:
                    continue

                # log(state, child, removable_sweets)

                sweets_remaining = list(sweets_remaining)
                for sweet in removable_sweets:
                    children_remaining[child] -= 1
                    sweets_remaining[sweet] -= 1
                    new_state = (tuple(children_remaining), tuple(sweets_remaining), )
                    if new_state in new_states:
                        continue
                    
                    prev[new_state] = state
                    actions[new_state] = (child, sweet)
                    new_states.add(new_state)

                    children_remaining[child] += 1
                    sweets_remaining[sweet] += 1

        states = new_states

    cur_state = ((0,)*n, (0,)*n, )

    if cur_state not in actions:
        return []

    res = []
    for _ in range(n):
        action = actions[cur_state]
        cur_state = prev[cur_state]

        res.append(action)

    return res[::-1]


                


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    nrr = read_matrix(k)  # and return as a list of list of int
    mrr = read_matrix(k+1)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(nrr, mrr, k)  # include input here

    if not res:
        print("Case #{}: {}".format(case_num+1, "IMPOSSIBLE"))   # Google and Facebook - case number required
        continue

    print("Case #{}: {}".format(case_num+1, "POSSIBLE"))   # Google and Facebook - case number required

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join("{} {}".format(x+1, y+2) for x,y in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
