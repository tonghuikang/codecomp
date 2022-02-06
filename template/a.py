#!/usr/bin/env python3
import sys
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
import getpass  # not available on codechef
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

def query(pos):
    print("{}".format(pos+1), flush=True)
    lst = input().split()
    if lst[0] == "AC":
        return lst[0]
    elif lst[0] == "R":
        return [(int(a),int(b)) for a,b in zip(lst[2::2], lst[3::2])]
    elif lst[0] == "F":
        return lst[0]
    else:
        assert False

def alert(pos):
    print("{}".format(pos+1), flush=True)
    sys.exit()


def solve_(n, m, start, base_move_count, edges):

    degrees = Counter()
    for a,b in edges:
        degrees[a] += 1
        degrees[b] += 1
    
    one_flag = len(degrees.values()) > len(degrees) // 4

    # your solution here
    cur_degree = -1
    prev_degree = -1
    first = True
    while True:
        if first:
            lst = input().split()
            q = [(int(a),int(b)) for a,b in zip(lst[2::2], lst[3::2])]
            first = False
        
        else:
            q = query(nex)

        prev_degree, cur_degree = cur_degree, len(q)

        log(q, prev_degree, cur_degree)
        if q == "AC":
            return
        if q == "F":
            return
        
        # no choice lmao
        if len(q) == 1:
            log("no choice")
            nex = 0
            continue
    
        # always optimal, if there is an unvisited node with degree one, visit
        flag = False
        for i,(d,f) in enumerate(q):
            if f == 0 and d == 1:
                log("degree one")
                nex = i
                flag = True
                break
        if flag:
            continue
        del flag
        
        unvisited = [(d,random.randint(0,100),i) for i,(d,f) in enumerate(q) if f == 0]

        # all adjacent nodes are already visited
        if not unvisited:
            visited = [(d,random.randint(0,100),i) for i,(d,f) in enumerate(q)]
            
            # node with the largest degree
            # visited.sort()
            # visited.reverse()
            # nex = visited[0][1]

            # nex = random.randint(0, len(q)-1)

            # if there are no unvisited neighbours, go one at random
            nex = 0
            # but avoid going back to a node with the same degree
            if visited[0][0] == prev_degree:
                nex = 1
            continue

        # only unvisited only
        if len(unvisited) == 1:
            nex = unvisited[0][2]
            continue

        unvisited.sort()

        # if an unvisited node has degree two, must go
        if unvisited[0][0] <= 2:
            log("degree two")
            nex = unvisited[0][2]
            continue

        # visit unvisited node with highest degree
        unvisited = unvisited[::-1]

        # visit random unvisited node
        # random.shuffle(unvisited)

        nex = unvisited[0][2]
        continue


    return


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    n, m, start, base_move_count = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    edges = read_matrix(m)  # and return as a list of list of int
    edges = minus_one_matrix(edges)

    res = solve(n, m, start, base_move_count, edges)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
