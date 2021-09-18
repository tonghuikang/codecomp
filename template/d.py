#!/usr/bin/env python3
# import math, random
# import functools, itertools, collections, heapq, bisect
from collections import defaultdict

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

# # if testing locally, print to terminal with a different color
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

# ---------------------------- template ends here ----------------------------

import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


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

# import random
def solve_(mrr,p,q):
    # your solution here

    flag = True
    # unique = set((x,y) for x,y in mrr)
    # if len(unique) < 20:
    #     flag = False


    mrr.sort(key=lambda x: (-x[0]/p -x[1]/q, x))
    # mrr.sort(key=lambda x: -x[1])
    # mrr.reverse()

    mincounts = defaultdict(lambda: 301)
    mincounts[0,0] = 0


    for a,b in mrr:
        new_count = defaultdict(lambda: 301)
        for (c,d),prev_count in mincounts.items():
            x,y = a+c,b+d
            x = min(p,x)
            y = min(q,y)
            new_count[x,y] = min(new_count[x,y], prev_count+1)

        for (x,y),count in new_count.items():
            mincounts[x,y] = min(mincounts[x,y], count)

        keys = list(mincounts.keys())
        keys.sort(key=lambda x:-x[1])

        # log(keys[:10])

        if flag:
            minseen = [301 for _ in range(p+1)]
            for x,y in keys:
                count = mincounts[x,y]
                if minseen[x] <= count:
                    del mincounts[x,y]
                minseen[x] = count

            keys = list(mincounts.keys())
            keys.sort(key=lambda x:-x[0])

            minseen = [301 for _ in range(q+1)]
            for x,y in keys:
                count = mincounts[x,y]
                if minseen[y] <= count:
                    del mincounts[x,y]
                minseen[y] = count

        flag = not flag



        # print(len(mincounts))

    # log(len(mincounts))

    res = mincounts[p,q]
    if res == 301:
        return -1

    return res


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
    p,q = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr,p,q)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
