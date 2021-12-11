#!/usr/bin/env python3
import sys
import getpass  # not available on codechef

import os
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


def binary_search(func_,       # condition function
                  first=True,  # else last
                  target=True, # else False
                  left=0, right=2**31-1) -> int:
    # https://leetcode.com/discuss/general-discussion/786126/
    # ASSUMES THAT THERE IS A TRANSITION
    # MAY HAVE ISSUES AT THE EXTREMES

    def func(val):
        # if first True or last False, assume search space is in form
        # [False, ..., False, True, ..., True]

        # if first False or last True, assume search space is in form
        # [True, ..., True, False, ..., False]
        # for this case, func will now be negated
        if first^target:
            return not func_(val)
        return func_(val)

    while left < right:
        mid = (left + right) // 2
        if func(mid):
            right = mid
        else:
            left = mid + 1
    if first:  # find first True
        return left
    else:      # find last False
        return left-1



def solve_(arr, brr, crr):
    # your solution here

    # binary search and sweep
    arr.sort()
    brr.sort(lambda x:x[1])
    crr.sort()

    def func(k):
        if k == 0:
            return True
        if k > len(arr):
            return False
        x_point = arr[k-1][0] + 1

        x_point_right = crr[-k][0] - 1
        cnt = 0
        for x,y in brr:
            if x_point <= x <= x_point_right:
                cnt += 1
            if cnt == k:
                return True

        cnt = 0
        for x,y in brr:
            if x < x_point:
                continue
            cnt += 1
            if cnt == k:
                break
        else:
            return False

        y_point = y + 1

        cnt = 0
        for x,y in crr:
            if x < x_point or y < y_point:
                continue
            cnt += 1

        if cnt < k:
            return False

        return True

    # log(func(0))
    # log(func(1))
    # log(func(2))
    # log(func(3))

    res = binary_search(func, left=0, right=len(arr)+1, first=False)

    # log(res)
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
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    arr = []
    brr = []
    crr = []
    for _ in range(k):
        x,y,i = list(map(int,input().split()))
        if i == 1:
            arr.append((x,y))
        if i == 2:
            brr.append((x,y))
        if i == 3:
            crr.append((x,y))

    res = 1

    r1 = solve(arr, brr, crr)  # include input here
    r2 = solve(brr, arr, crr)  # include input here
    r3 = solve(crr, arr, brr)  # include input here

    log(r1,r2,r3)

    res = max([res, r1, r2, r3])

    def reverse_and_negate(xrr):
        return [(-x,y) for x,y in xrr]

    arr = reverse_and_negate(arr)
    brr = reverse_and_negate(brr)
    crr = reverse_and_negate(crr)

    r1 = solve(arr, brr, crr)  # include input here
    r2 = solve(brr, arr, crr)  # include input here
    r3 = solve(crr, arr, brr)  # include input here

    log(r1,r2,r3)

    res = max([res, r1, r2, r3])

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res*3)
