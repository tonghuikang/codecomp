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

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

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



def topological_sort(map_from_node_to_nodes, all_nodes=set()):
    # leetcode.com/problems/course-schedule-ii/
    indegree_counter = defaultdict(int)
    for lst in map_from_node_to_nodes.values():
        for v in lst:
            indegree_counter[v] += 1

    if not all_nodes:  # assume all nodes are found in the map
        all_nodes = set(indegree_counter.keys()) | set(map_from_node_to_nodes)

    dq = deque([node for node in all_nodes if node not in indegree_counter])

    res = []
    while dq:
        cur = dq.popleft()
        res.append(cur)
        for nex in map_from_node_to_nodes[cur]:
            indegree_counter[nex] -= 1
            if indegree_counter[nex] == 0:
                dq.append(nex)
    return res if len(res) == len(all_nodes) else []


def solve_(arr, n):
    # your solution here

    # is_destined = {}
    g = defaultdict(list)

    for a,b,c in arr:
    #     is_destined[b,c] = a == 1  # deducted one previously
    #     is_destined[c,b] = a == 1
        g[b].append(c)
        g[c].append(b)

    color = {}
    for i in range(n):
        if i in color:
            continue
        color[i] = 1
        stack = [i]
        while stack:
            cur = stack.pop()
            for nex in g[cur]:
                if nex in color:
                    if color[nex] == color[cur]:
                        return False, []
                    continue
                color[nex] = 1 - color[cur]
                stack.append(nex)

    # 0 = faceleft
    # 1 = faceright

    dirs = defaultdict(list)

    for a,b,c in arr:
        # deducted one previously
        is_destined = a == 1

        if is_destined:
            if color[b] == 1:
                # b faceright posleft, c faceleft posright
                dirs[b].append(c)
            else:
                dirs[c].append(b)

        else:
            if color[b] == 1:
                # b faceright posright, c faceleft posleft
                dirs[c].append(b)
            else:
                dirs[b].append(c)

    arr = topological_sort(dirs, set(range(n)))
    posting = {x:i for i,x in enumerate(arr)}

    # log(arr)
    # log(color)

    res = []
    for i in range(n):
        if color[i] == 0:
            dirr = "L"
        else:
            dirr = "R"
        pos = posting[i]
        res.append("{} {}".format(dirr, pos))

    return True, res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    boo, res = solve(mrr, n)  # include input here

    if not boo:
        print(no)
        continue

    print(yes)
    
    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
