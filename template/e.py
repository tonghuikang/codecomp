#!/usr/bin/env python3
import sys
import heapq
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


def solve_(n,mrr,arr):
    # prune to the largest number, and the next etc
    assert len(mrr) == n-1
    assert len(arr) == n

    # cast all unique values to zero
    # if there is three of the largest number, the answer is all largest
    #   not possible to break between three of them at once

    edges_to_idx = {}
    res = [-1 for _ in range(n)]
    g = [[] for _ in range(n)]

    for i,(a,b) in enumerate(mrr):
        edges_to_idx[a,b] = i
        edges_to_idx[b,a] = i
        g[a].append(b)
        g[b].append(a)

    acnt = Counter(arr)
    for i in range(n):
        if acnt[arr[i]] == 1:
            arr[i] = 0
    # log(arr)

    maxval = max(arr)
    res = [maxval for _ in range(n-1)]
    if acnt[maxval] > 2:
        return res

    assert acnt[maxval] == 2

    # find the path between the two maximums
    start = arr.index(maxval)
    queue = deque([start])
    parent = {start:-1}

    flag = True
    while queue and flag:
        cur = queue.popleft()
        # log(cur, parent)
        for nex in g[cur]:
            if nex in parent:
                continue
            parent[nex] = cur
            queue.append(nex)
            if arr[nex] == maxval:
                flag = False
                break

    assert start != nex
    assert arr[nex] == maxval
    assert arr[start] == maxval
    # log("start", start, arr.index(maxval))
    # log(parent)
    cur = nex
    path = [cur]
    while parent[cur] != -1:
        cur = parent[cur]
        path.append(cur)

    assert path[0] == nex
    assert path[-1] == start
    assert len(path) >= 2

    # log(path)

    for a,b in zip(path, path[1:]):
        edge_idx = edges_to_idx[a,b] 
        res[edge_idx] = -1

    # leader classification
    visited = set(path)
    leader = {x:x for x in path}
    stack = list(visited)
    while stack:
        cur = stack.pop()
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            stack.append(nex)
            leader[nex] = leader[cur]
    
    leading = defaultdict(list)
    for x,ldr in leader.items():
        if arr[x] >= 0:
            leading[ldr].append(arr[x])

    # log(path)
    log(leading)

    left_counter = Counter()
    left_duplicate_candidates = []  # maxheap

    right_counter = Counter()
    right_duplicate_candidates = [] # maxheap

    count_check = 0
    for val in leading[path[0]]:
        left_counter[val] += 1
        count_check += 1

    for x in path[1:]:
        for val in leading[x]:
            right_counter[val] += 1
            count_check += 1
    
    assert count_check == n

    left_duplicate_candidates = [-x for x in left_counter.keys()]
    right_duplicate_candidates = [-x for x in right_counter.keys()]

    left_duplicate_candidates.sort()
    right_duplicate_candidates.sort()

    for a,b in zip(path, path[1:]):

        while left_duplicate_candidates and left_counter[-left_duplicate_candidates[0]] < 2:
            heapq.heappop(left_duplicate_candidates)
        maxval = 0
        if left_duplicate_candidates:
            val = -left_duplicate_candidates[0]
            maxval = max(maxval, val)

        while right_duplicate_candidates and right_counter[-right_duplicate_candidates[0]] < 2:
            heapq.heappop(right_duplicate_candidates)
        if right_duplicate_candidates:
            val = -right_duplicate_candidates[0]
            maxval = max(maxval, val)

        edge_idx = edges_to_idx[a,b]
        res[edge_idx] = maxval

        # transfer
        for val in leading[b]:
            right_counter[val] -= 1
            left_counter[val] += 1
            heapq.heappush(left_duplicate_candidates, -val)

    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

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
    arr = list(map(int,input().split()))
    mrr = minus_one_matrix(mrr)

    res = solve(n,mrr,arr)  # include input here

    assert len(res) == n-1

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
