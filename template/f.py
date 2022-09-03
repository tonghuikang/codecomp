#!/usr/bin/env python3
import sys
from collections import defaultdict, deque
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
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
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


def solve_(n,q,mrr,qrr):
    # your solution here
    g = defaultdict(list)
    for a,b in mrr:
        g[a].append(b)
        g[b].append(a)

    queue = deque([0])
    visited = set([0])
    while queue:
        cur = queue.popleft()
        for nex in g[cur]:
            if nex in visited:
                continue
            queue.append(nex)
            visited.add(nex)
        
    log(cur)
    start = cur

    prev = {}

    queue = deque([start])
    visited = set([start])
    while queue:
        cur = queue.popleft()
        for nex in g[cur]:
            if nex in visited:
                continue
            prev[nex] = cur
            queue.append(nex)
            visited.add(nex)
        
    end = cur
    log(end)

    series = [end]
    while cur in prev:
        cur = prev[cur]
        series.append(cur)

    log(series)

    ancestors = defaultdict(list)
    depth = {}
    header = {}
    header[series[0]] = 0
    header[series[-1]] = len(series) - 1
    depth[series[0]] = 0
    depth[series[-1]] = 0

    for header_idx,(a,b,c) in enumerate(zip(series, series[1:], series[2:]), start=1):
        visited = set([a,b,c])
        queue = deque([b])
        depth[b] = 0
        prev = {}
        while queue:
            cur = queue.popleft()
            header[cur] = header_idx
            for nex in g[cur]:
                if nex in visited:
                    continue
                prev[nex] = cur
                depth[nex] = depth[cur] + 1
                ancestors[nex].append(cur)

                anc = cur
                idx = 0
                while len(ancestors[anc]) >= len(ancestors[nex]):
                    ancestors[nex].append(ancestors[anc][idx])
                    anc = ancestors[anc][idx]
                    idx += 1
                
                queue.append(nex)
                visited.add(nex)

    log(ancestors)
    log([depth[x] for x in range(n)])
    log([header[x] for x in range(n)])

    allres = []
    for a,b in qrr:
        b += 1
        res = -2
        
        if depth[a] <= b:
            header_idx = header[a]
            dist = b - depth[a]
            log(dist)
            if header_idx - dist >= 0:
                res = series[header_idx - dist]
            if header_idx + dist < len(series):
                res = series[header_idx + dist]
        else:
            anc_idx = 0
            cur = a
            while b:
                if b%2:
                    cur = ancestors[cur][anc_idx]
                else:
                    pass
                b = b // 2
                anc_idx += 1
            res = cur
        
        allres.append(res)

    return allres


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

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
    mrr = read_matrix(n-1)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)
    q = int(input())
    qrr = read_matrix(q)  # and return as a list of list of int
    qrr = minus_one_matrix(qrr)

    res = solve(n,q,mrr,qrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = "\n".join(str(x+1) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
