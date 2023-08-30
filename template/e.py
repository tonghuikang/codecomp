#!/usr/bin/env python3
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
# abc = "abcdefghijklmnopqrstuvwxyz"
# abc_map = {c:i for i,c in enumerate(abc)}
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
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


class DisjointSet:
    # github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
    # faster implementation of DSU
    def __init__(self, n: int = 0) -> None:
        if n > 0:  # constant size DSU
            self.parent_or_size = [-1]*n
        else:
            # WARNING: non-negative numeric elements only
            self.parent_or_size = defaultdict(lambda: -1)

    def union(self, a: int, b: int) -> int:
        x = self.find(a)
        y = self.find(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def find(self, a: int) -> int:
        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )
        return a

    def size(self, a: int) -> int:
        return -self.parent_or_size[self.find(a)]


def solve_ref(n,m,k,arr,mrr):
    # your solution here
 
    minres = e18
    for q in arr:
        g = [set() for _ in range(n)]
        f = [set() for _ in range(n)]
        for a,b in mrr:
            g[a].add(b)
            f[b].add(a)
        
        queue = []
        start = 0
    
        for i in range(n):
            if len(f[i]) == 0:
                queue.append((arr[i], i))
    
        heapq.heapify(queue)
    
        start = queue[0][0]
    
        while queue:
            hour, cur = heapq.heappop(queue)
            log(hour, cur)
            for nex in g[cur]:
                f[nex].remove(cur)
                if len(f[nex]) == 0:
                    nex_hour = arr[nex]
                    if nex_hour >= hour:
                        heapq.heappush(queue, ((hour // k) * k + nex_hour, nex))
                    else:
                        heapq.heappush(queue, ((hour // k) * k + nex_hour + k, nex))

            minres = min(minres, res)
 
    log(minres)
    return minres


def solve_(n,m,k,arr,mrr):
    # your solution here

    # for each dependency group there is a start and end time

    ds = DisjointSet()
    g = [set() for _ in range(n)]
    g2 = [set() for _ in range(n)]
    f = [set() for _ in range(n)]
    f2 = [set() for _ in range(n)]
    for a,b in mrr:
        g[a].add(b)
        g2[a].add(b)
        f[b].add(a)
        f2[b].add(a)
        ds.union(a,b)

    for x in range(n):
        ds.find(x)
    leaders = defaultdict(list)
    for x in range(n):
        leaders[ds.find(x)].append(x)

    times = []
    for group in leaders.values():
        queue = []
        start = 0

        for i in group:
            if len(f[i]) == 0:
                queue.append((arr[i], i))

        heapq.heapify(queue)

        starts = {}

        while queue:
            hour, cur = heapq.heappop(queue)
            starts[cur] = hour
            # log(hour, cur)
            for nex in g[cur]:
                f[nex].remove(cur)
                if len(f[nex]) == 0:
                    if arr[nex] >= arr[cur]:
                        heapq.heappush(queue, ((hour // k) * k + arr[nex], nex))
                    else:
                        heapq.heappush(queue, ((hour // k) * k + arr[nex] + k, nex))


        # if all the tasks that depend on yours is completed at least k hours in the future
        # you can bring yours forward

        # log(starts)

        stack = []
        for cur in group:
            if len(g[cur]) == 0:
                stack.append(cur)

        while stack:
            cur = stack.pop()
            # log(cur)

            if len(g[cur]) > 0:            
                max_start_time = e18
                for nex in g[cur]:
                    if arr[cur] <= arr[nex]:
                        start_time = (starts[nex] // k) * k + arr[cur]
                    else:
                        start_time = (starts[nex] // k) * k + arr[cur] - k
                    max_start_time = min(max_start_time, start_time)
                starts[cur] = max_start_time

            for nex in f2[cur]:
                g2[nex].remove(cur)
                if len(g2[nex]) == 0:
                    stack.append(nex)

        # log(starts)

        times.append((min(starts.values()), max(starts.values())))

    # log(times)

    times.sort()
    maxend = max(end for _, end in times)
    minres = maxend - times[0][0]

    for (a,b),(x,y) in zip(times, times[1:]):
        maxend = max(maxend, b + k)
        res = maxend - x
        minres = min(minres, res)        

    return minres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,m,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(m)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    res = solve(n,m,k,arr,mrr)  # include input here

    assert res == solve_ref(n,m,k,arr,mrr)

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
