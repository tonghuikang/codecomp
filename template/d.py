#!/usr/bin/env python3
import sys
# import getpass  # not available on codechef
import heapq
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

# M9 = 10**9 + 7  # 998244353
# yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
# MAXINT = sys.maxsize

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


# ---------------------------- template ends here ----------------------------


if True:
    # your solution here
    k = int(input())
    arr = []
    brr = []
    for _ in range(k):
        crr = map(int,input().split())
        arr.append(next(crr))
        brr.append(list(crr))
    arr = tuple(x-1 for x in arr)
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    k = int(input())
    banned = set(tuple(x-1 for x in map(int,input().split())) for _ in range(k))

    n = len(arr)
    queue = [[-sum(row[-1] for row in brr), -1, tuple(arr)]]
    visited = set()

    idx = 0
    while queue:
        idx += 1
        score, _, comb = heapq.heappop(queue)
        # print(score, comb)
        # log(score, comb)
        if comb not in banned:
            comb = [x+1 for x in comb]
            res = " ".join(str(x) for x in comb)
            print(res)
            sys.exit()
        comb = list(comb)
        for i in range(n):
            combi = comb[i]
            if combi == 0:
                continue
            diff = brr[i][combi - 1] - brr[i][combi]
            comb[i] -= 1
            score -= diff
            tuple_comb = tuple(comb)
            if tuple_comb in visited:
                continue
            heapq.heappush(queue, (score, idx, tuple(comb)))
            visited.add(tuple_comb)
            comb[i] += 1
            score += diff
