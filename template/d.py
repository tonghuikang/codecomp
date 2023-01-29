#!/usr/bin/env python3
import sys
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
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


def solve_(n, arr):
    # your solution here
    arr = [0] + arr

    # you can't jump to any loops, any of your ancestors
    g = [[] for _ in range(n+1)]

    for i,x in enumerate(arr[1:], start=1):
        nex = i+x
        if 1 <= nex <= n:
            g[nex].append(i)

    # positions in loops
    visited = set()
    loop_set = set()
    for i,x in enumerate(arr[1:], start=1):
        if i in visited:
            continue
        cur = i
        cur_visited = set([cur])
        while True:
            nex = arr[cur] + cur
            if not (1 <= nex <= n):
                visited.update(cur_visited)
                break
            if nex in cur_visited or nex in loop_set:
                visited.update(cur_visited)
                loop_set.update(cur_visited)
                break
            cur_visited.add(nex)
            cur = nex

    # log(loop_set)
    # log(g)

    cur = 1
    cyclic = True

    res = n * (2*n + 1)

    seen = loop_set
    pathset = set()
    while True:
        stack = [cur]
        pathset.add(cur)
        while stack:
            a = stack.pop()
            seen.add(a)
            for b in g[a]:
                if b in seen:
                    continue
                seen.add(b)
                stack.append(b)
        # log(cur, seen)
        res -= len(seen)
        cur = cur + arr[cur]
        if not (1 <= cur <= n):
            cyclic = False
            break
        if cur in pathset:
            break

    # log("cyclic", cyclic)

    if not cyclic:
        return res


    return len(pathset) * (2*n+1 - len(loop_set)) 

    


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
