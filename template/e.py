#!/usr/bin/env python3
import sys
from collections import defaultdict

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

# https://codeforces.com/blog/entry/80158?locale=en
from types import GeneratorType
def bootstrap(f, stack=[]):
    # usage - please remember to YIELD to call and return
    '''
    @bootstrap
    def recurse(n):
        if n <= 0:
            yield 0
        yield (yield recurse(n-1)) + 2

    res = recurse(10**5)
    '''
    def wrappedfunc(args):
        if stack:
            return f(args)
        else:
            to = f(args)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    if stack:
                        stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc



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

    g = defaultdict(list)
    for a,b in mrr:
        g[a].append(b)
        g[b].append(a)

    del mrr

    visited = set()

    # + number of children that is not a bud
    # - number of buds
    # + 1


    @bootstrap
    def is_bud(cur):
        total_count_buds = 0
        total_children_not_a_bud = 0

        num_children = 0
        num_children_not_bud = 0

        # children_is_bud = []
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            child_is_bud, count_buds, children_not_a_bud = yield is_bud(nex)

            num_children += 1
            total_count_buds += count_buds
            total_children_not_a_bud += children_not_a_bud

            if not child_is_bud:
                num_children_not_bud += 1

        # this is not a bud
        if num_children == 0 or num_children_not_bud == 0:
            yield False, total_count_buds, total_children_not_a_bud + num_children_not_bud

        # this is a bud
        yield True, total_count_buds + 1, total_children_not_a_bud + num_children_not_bud

    visited.add(1)
    _, total_count_buds, total_children_not_a_bud = is_bud(1)

    # log(num_children_not_a_bud)
    # log(buds)
    # log(non_buds)

    res = total_children_not_a_bud - total_count_buds + 1
    all_res.append(res)

all_res = "\n".join(str(x) for x in all_res)
print(all_res)
