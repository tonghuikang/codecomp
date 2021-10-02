#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
from collections import defaultdict, deque
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


def solve_(mrr):
    # if len(mrr) == 1:
    #     return 1
    # your solution here

    g = defaultdict(list)

    for a,b in mrr:
        g[a].append(b)
        g[b].append(a)


    queue = deque([0])
    visited = set(queue)
    while queue:
        cur = queue.popleft()
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            queue.append(nex)

    queue = deque([cur])
    visited = set(queue)
    while queue:
        cur = queue.popleft()
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            queue.append(nex)

    e1 = cur
    queue = deque([e1])
    d1 = {e1:0}
    while queue:
        cur = queue.popleft()
        for nex in g[cur]:
            if nex in d1:
                continue
            d1[nex] = d1[cur] + 1
            queue.append(nex)

    e2 = cur
    queue = deque([e2])
    d2 = {e2:0}
    while queue:
        cur = queue.popleft()
        for nex in g[cur]:
            if nex in d2:
                continue
            d2[nex] = d2[cur] + 1
            queue.append(nex)

    log(d1)
    log(d2)

    d1_arr = [0 for _ in range(len(mrr) + 1)]
    d2_arr = [0 for _ in range(len(mrr) + 1)]
    for k,v in d1.items():
        d1_arr[k] = v
    for k,v in d2.items():
        d2_arr[k] = v
    log(d1_arr)
    log(d2_arr)

    maxd = max(d1_arr)

    endpoints = set()
    for i,(a,b) in enumerate(zip(d1_arr, d2_arr)):
        if a == maxd or b == maxd:
            endpoints.add(i)

    center_point = -1
    for i,(a,b) in enumerate(zip(d1_arr, d2_arr)):
        if a == b == maxd/2:
            # assume only one center point
            assert center_point == -1
            # this is the center point
            center_point = i

    log("center_point", center_point)

    if center_point != -1:
        group_counts = []
        visited = set([center_point])
        for start in g[center_point]:
            group_count = 0
            visited.add(start)
            queue = deque([start])
            while queue:
                cur = queue.popleft()
                if cur in endpoints:
                    group_count += 1
                for nex in g[cur]:
                    if nex in visited:
                        continue
                    visited.add(nex)
                    queue.append(nex)
            group_counts.append(group_count)
        log(group_counts)

        # select one or zero from each group
        res = 1
        for x in group_counts:
            res = res * (x+1)
            res = res%998244353

        log(res)

        # select only one group
        for x in group_counts:
            res -= x

        # select none of the groups
        res -= 1

        return res

    # there is a center edge
    g1_size = 0
    g2_size = 0
    for a,b in zip(d1_arr, d2_arr):
        if a == maxd:
            g1_size += 1
        if b == maxd:
            g2_size += 1
        assert not a == b == maxd

    log(g1_size, g2_size)

    return (g1_size * g2_size) % 998244353



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
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k-1)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    res = solve(mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res % 998244353)
