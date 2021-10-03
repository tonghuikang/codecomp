#!/usr/bin/env python3
import sys, getpass
from random import choice
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

# ---------------------------- template ends here ----------------------------

def query(arr):
    print("? {}".format(" ".join(str(pos+1) for pos in arr)), flush=True)
    response = int(input())
    return response

def alert(a,b):
    print("! {} {}".format(a+1,b+1), flush=True)
    sys.exit()

# -----------------------------------------------------------------------------

# read line as an integer
k = int(input())

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

mrr = read_matrix(k-1)  # and return as a list of list of int
mrr = minus_one_matrix(mrr)
g = defaultdict(list)

for a,b in mrr:
    g[a].append(b)
    g[b].append(a)

target = query(range(k))
remainder = set(list(range(k)))

eliminated = set()

def select_half(remainder, eliminated):
    start = choice(tuple(remainder))
    stack = [start]
    selected = set(stack)
    while len(selected) < len(remainder) / 2:
        # print(selected, stack)
        if stack:
            cur = stack.pop()
            for nex in g[cur]:
                if nex in eliminated:
                    continue
                if nex in selected:
                    continue
                selected.add(nex)
                stack.append(nex)
                if len(selected) >= len(remainder) / 2:
                    break
        if not stack:
            cur = choice(tuple(remainder - selected))
            stack.append(cur)

    return selected

def propagate_selected(selected, eliminated):
    # include edges between selected and remainder
    # but do not include edges between eliminated and selected
    addition = set()
    for a,b in mrr:
        if a not in eliminated and (a not in selected) and b in selected:
            addition.add(b)
        if b not in eliminated and (b not in selected) and a in selected:
            addition.add(a)
    return addition

remainder = set(range(k))
for _ in range(11):
    selected = select_half(remainder, eliminated)
    queried = query(list(selected))

    if queried == target:
        eliminated.update(remainder - selected)
        remainder = selected

    else:
        addition = propagate_selected(selected, eliminated)
        # print(addition)
        selected = (remainder - selected) | addition
        eliminated.update(remainder - selected)
        remainder = selected

        # print(remainder, addition)

    if len(remainder) == 2:
        remainder = list(remainder)
        alert(remainder[0], remainder[1])

remainder = list(remainder)
alert(remainder[0], remainder[1])
