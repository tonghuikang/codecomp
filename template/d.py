#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


# class FastIO(IOBase):
#     newlines = 0

#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None

#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()

#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()

#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)


# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")


# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")

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


def solve_(mrr, m, n):
    # your solution here

    allow_red_all = set(range(m-1))
    allow_blue_all = set(range(m-1))

    red_flag = True
    blue_flag = True

    res_color = ""

    for i in range(n):
        row = mrr[i]
        log(row)
        pmin = [row[0]]
        pmax = [row[0]]
        for x in row[1:]:
            pmin.append(min(pmin[-1], x))
            pmax.append(max(pmax[-1], x))

        smin = [row[-1]]
        smax = [row[-1]]
        for x in (row[:-1])[::-1]:
            smin.append(min(smin[-1], x))
            smax.append(max(smax[-1], x))
        smin.reverse()
        smax.reverse()

        allow_red = set()
        allow_blue = set()
        for i,(a,b) in enumerate(zip(pmin, smax[1:])):
            if a > b:
                allow_red.add(i)
        for i,(a,b) in enumerate(zip(pmax, smin[1:])):
            if a < b:
                allow_blue.add(i)

        log(allow_red)
        log(allow_blue)
        log(allow_red_all)
        log(allow_blue_all)
        log()

        assert not ((len(allow_red) > 0) and (len(allow_blue) > 0))

        if allow_red:
            allow_red_all = allow_red_all & allow_red
            res_color += "R"
            red_flag = False
        elif allow_blue:
            allow_blue_all = allow_blue_all & allow_blue
            res_color += "B"
            blue_flag = False
        else:
            allow_red_all = set()
            allow_blue_all = set()

    allow_all = allow_red_all & allow_blue_all
    if not allow_all:
        log("no eligible columns")
        return "NO"

    if blue_flag or red_flag:
        log("need at least one each")
        return "NO"

    log(allow_all)
    res_col = list(allow_all)[0] + 1

    return res_color, res_col


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    n,m = list(map(int,input().split()))
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr, m, n)  # include input here

    if res == "NO":
        print(res)
        continue

    print("YES")
    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
