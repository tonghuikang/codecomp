#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
# import math, random
# import functools, itertools, collections, heapq, bisect
from collections import defaultdict
# input = sys.stdin.readline  # to read input quickly
import os
import sys
from io import BytesIO, IOBase

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy
BUFSIZE = 8192


M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
# OFFLINE_TEST = getpass.getuser() == "hkmac"
OFFLINE_TEST = False  # codechef does not allow getpass
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



class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")



# minmax

def solve_(minrr, maxrr, edges):
    # your solution here

    g = defaultdict(list)
    for a,b in edges:
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    
    # maxres = 0

    # for boo in range(2):
    #     stack = [0]
    #     status = [-1]*len(mrr)
    #     status[0] = boo
    #     curres = 0
    #     while stack:
    #         cur = stack.pop()
    #         # log(cur)
    #         for nex in g[cur]:
    #             # log(nex)
    #             if status[nex] >= 0:
    #                 continue
    #             status[nex] = 1-status[cur]
    #             stack.append(nex)
    #             val = abs(mrr[nex][status[nex]] - mrr[cur][status[cur]])
    #             # log(val)
    #             # log(nex)
    #             curres += val
                
    #     maxres = max(maxres, curres)

    # return maxres

    entered = set([0])
    exiting = set()
    prev = [-1]*len(arr)
    resmincur = [0]*len(arr)
    resmaxcur = [0]*len(arr)

    def operate(cur, nex):
        if cur == -1:
            return
        resminnex = resmincur[nex]
        resmaxnex = resmaxcur[nex]
        resmax = max(resminnex + abs(minrr[nex] - maxrr[cur]), resmaxnex + abs(maxrr[nex] - maxrr[cur]))
        resmin = max(resmaxnex + abs(maxrr[nex] - minrr[cur]), resminnex + abs(minrr[nex] - minrr[cur]))
        resmincur[cur] += resmin
        resmaxcur[cur] += resmax

    stack = [0]
    while stack:
        cur = stack[-1]
        if cur in exiting:
            stack.pop()
            operate(prev[cur], cur)
            continue
        for nex in g[cur]:
            if nex in entered:
                continue
            entered.add(nex)
            stack.append(nex)
            prev[nex] = cur
        exiting.add(cur)

    return max(resmincur[0], resmaxcur[0])


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

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
    mrr = read_matrix(k)  # and return as a list of list of int
    arr, brr = zip(*mrr)
    del mrr
    edges = read_matrix(k-1)  # and return as a list of list of int
    # edges = minus_one_matrix(edges)

    res = solve(arr, brr, edges)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)