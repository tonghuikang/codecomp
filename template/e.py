#!/usr/bin/env python3
import sys

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]


BUFSIZE = 8192

import os
from io import BytesIO, IOBase
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


all_res = []
cases = []
# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # your solution here
    k = int(input())
    cases.append(read_matrix(k-1))  # and return as a list of list of int


for mrr in cases:
    # log(k)
    # log(mrr)
    k = len(mrr)

    g = [[] for i in range(k+2)]
    for a,b in mrr:
        g[a].append(b)
        g[b].append(a)

    del mrr

    visited = set()

    # + number of children that is not a bud
    # - number of buds
    # + 1

    # global total_children_not_a_bud
    # global total_count_buds
    total_children_not_a_bud = 0
    total_count_buds = 0

    # buds = set()
    # children_who_are_not_buds = set()
    has_children = [False for _ in range(k+2)]
    has_children_who_are_not_buds = [False for _ in range(k+2)]


    start = 1
    if True:
        # hacked this out due to strict time limit because recursive dfs resulted in TLE
        # https://codeforces.com/contest/1528/problem/A
        # instead of returning a value, read and update an external data structure instead
        entered = set([start])
        exiting = set()
        stack = [start]
        prevs = {start: 0}

        while stack:
            cur = stack[-1]
            if cur in exiting:
                stack.pop()
                if cur in prevs:
                    prev = prevs[cur]
                    if has_children[cur] and has_children_who_are_not_buds[cur]:
                        total_count_buds += 1
                        # buds.add(cur)
                    else:
                        # children_who_are_not_buds.add(cur)
                        has_children_who_are_not_buds[prev] = True
                        if cur != 1:
                            total_children_not_a_bud += 1

                    has_children[prev] = True
                continue
            for nex in g[cur]:
                if nex in entered:
                    continue
                entered.add(nex)
                stack.append(nex)
                prevs[nex] = cur
            exiting.add(cur)


    # def return_operation(prev, cur):
        # global total_children_not_a_bud
        # global total_count_buds


    # g[0].append(1)
    # log(num_children_not_a_bud)
    # log(buds)
    # log(non_buds)
    # dfs_bare_bones(1, g, return_operation)
    # children_who_are_not_buds.discard(1)

    # print()
    # print(buds)
    # print(children_who_are_not_buds)

    res = total_children_not_a_bud - total_count_buds + 1
    all_res.append(res)

all_res = "\n".join(str(x) for x in all_res)
print(all_res)
