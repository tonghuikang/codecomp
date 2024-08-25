#!/usr/bin/env python3
import sys

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}
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
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x - 1 for x in arr]


def minus_one_matrix(mrr):
    return [[x - 1 for x in row] for row in mrr]


# ---------------------------- template ends here ----------------------------


def get_mex2(arr):
    arr = sorted(set(arr))

    hole_one = -1
    expected = 0

    for x in arr + [999_999_997, 999_999_998, 999_999_999]:
        if x == expected:
            expected += 1
            continue
        
        if x != expected and hole_one == -1:
            hole_one = expected
            expected += 1
            if x != expected:
                return hole_one, expected
            expected += 1
            continue
        if x != expected:
            return hole_one, expected
        


def solve_(n,m,mrr):
    # your solution here

    maxb = 0

    edges = [-1 for _ in range(n+10)]
    zero_applicable = []

    for _, *row in mrr:
        a,b = get_mex2(row)
        maxb = max(maxb,b)

        if edges[a] != -1:
            zero_applicable.append(a)

        edges[a] = max(edges[a], b)

    res = 0
    empties = []

    for i in range(n+1):
        if edges[i] == -1:
            empties.append(i)
            continue
        
        cur = i
        sequence = [cur]
        while edges[cur] != -1 and edges[cur] != cur:
            cur = edges[cur]
            sequence.append(cur)
        
        for node in sequence:
            edges[node] = cur

        # log(i, cur)

        # res += cur

    maxempty = 0
    for x in zero_applicable:
        maxempty = max(maxempty, edges[x])
    # log(empties, zero_applicable, maxempty)

    for i in range(n+1):
        if edges[i] == -1:
            # empties.append(i)
            res += max(i, maxempty)
            continue
        
        cur = i
        sequence = [cur]
        while edges[cur] != -1 and edges[cur] != cur:
            cur = edges[cur]
            sequence.append(cur)
        
        for node in sequence:
            edges[node] = cur

        # log(i, cur)

        res += max(maxempty, cur)


    if m > n:
        res += m * (m+1) // 2 - n * (n+1) // 2

    return res


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
    n, m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,m,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
