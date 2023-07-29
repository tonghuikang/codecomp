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


def encode(a,b,c):
    return 100*100*a + 100*b + c

def decode(x):
    a,bc = divmod(x,100)
    b,c = divmod(bc,100)
    return a,b,c

def solve_(mrr):
    # your solution here

    mapping = [-1 for _ in range(100*100*100)]

    for i,(a,b,c,p,q,r) in enumerate(mrr):
        for x in range(a,p):
            for y in range(b,q):
                for z in range(c,r):
                    mapping[encode(x,y,z)] = i

    adj = [set() for _ in range(len(mrr))]

    for x in range(100):
        for y in range(100):
            for z in range(100):
                f = mapping[encode(x,y,z)]
                if f == -1:
                    continue
                for dx,dy,dz in [(1,0,0),(0,1,0),(0,0,1)]:
                    xx = x+dx
                    yy = y+dy
                    zz = z+dz
                    if xx >= 100 or yy >= 100 or zz >= 100:
                        continue
                    g = mapping[encode(xx,yy,zz)]
                    if g != -1 and f != g:
                        adj[f].add(g)
                        adj[g].add(f)

    return [len(x) for x in adj]


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
