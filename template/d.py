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
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
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

class Dinic:
    # codeforces.com/contest/1473/submission/104332748
    # max flow algorithm
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# last = [-1 for i in range(101)]

# G = Dinic(n+2)

# res = 0
# for i in range(n):
#     if b[i] > 0:
#         res += b[i]
#         G.add_edge(i+1,n+1,b[i])
#     else:
#         G.add_edge(0,i+1,-b[i])

#     pre = last[a[i]]
#     if pre!=-1:
#         G.add_edge(pre+1,i+1,10**15)
#     for j in range(pre+1,i):
#         if a[i]%a[j]==0:
#             G.add_edge(j+1,i+1,10**15)

#     last[a[i]] = i

# print(res-G.flow(0,n+1))



def solve_(arr, brr, h, w, x, y):
    
	# your solution here
	diff = sum(sum(a != b for a,b in zip(row1, row2)) for row1, row2 in zip(arr, brr))
	# log(diff)

	for z in range(2):
		pos = set()
		G = Dinic(h*w+2)
		for i in range(h):
			for j in range(w):
				if arr[i][j] == "M" and brr[i][j] == "G" and (i+j)%2 == 1-z:
					pos.add((i,j))
				if arr[i][j] == "G" and brr[i][j] == "M" and (i+j)%2 == z:
					pos.add((i,j))
		# log(pos)
		for x,y in pos:
			p1 = x*w + y + 1

			if (x+y)%2:
				G.add_edge(p1,h*w+1,1)
				continue
			else:
				G.add_edge(0,p1,1)

			for dx, dy in d4:
				xx = x+dx
				yy = y+dy
				if (xx,yy) in pos:
					p2 = xx*w + yy + 1
					G.add_edge(p1,p2,1)
	
		r = G.flow(0,h*w+1)
		# log(r)
		diff -= r
	
	return diff


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
    h,w,x,y = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    arr = read_strings(h)  # and return as a list of str
    brr = read_strings(h)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, brr, h, w, x, y)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)