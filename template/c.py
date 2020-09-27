# obtained from https://codeforces.com/profile/anishde85, original sources to be determined
# ---------------------------iye ha aam zindegi---------------------------------------------
import math
import random
import heapq, bisect
import sys
from collections import deque, defaultdict
from fractions import Fraction
import sys
import threading
from collections import defaultdict
# threading.stack_size(1<<27)
mod = 10**9 + 7
mod1 = 998244353

# ------------------------------warmup----------------------------
import os
import sys
from io import BytesIO, IOBase
# sys.setrecursionlimit(300000)

BUFSIZE = 8192

import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr):  # fix inputs here
    console("----- solving ------")

    # if it occurs in every a, it occurts at every a+1
    d = defaultdict(list)

    for i,a in enumerate(arr):
        d[a].append(i)

    minval = {}

    for k,v in d.items():
        v = [-1] + v + [len(arr)]
        minval[k] = max(b-a for a,b in zip(v,v[1:]))

    minval2 = sorted([(v,k) for k,v in minval.items()])
    console(minval2)

    curmin = 10**10
    res = []
    cur = 0


    for v,k in minval2:
        if v == cur:
            continue

        while cur < v-1 and cur < len(arr):
            cur += 1
            res.append(curmin)

        curmin = min(curmin, k)
        cur += 1
        res.append(curmin)

    console(res)

    while cur < len(arr):
        cur += 1
        res.append(curmin)

    res = [-1 if x == 10**10 else x for x in res]

    # return a string (i.e. not a list or matrix)
    return res


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

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

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    res = " ".join(str(x) for x in res)
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
