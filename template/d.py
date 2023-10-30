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

def f(x):
    y = 0
    while x >= 2:
        x //= 2
        y += 1
    return y

def g(x):
    if x < 4:
        return "x must be greater or equal to 4"
    fx = f(x)
    z = 0
    product = 1
    while product * fx <= x:
        product *= fx
        z += 1
    return z

def binary_search(
    func_,  # condition function
    first=True,  # else last
    target=True,  # else False
    left=0,
    right=2**31 - 1,
) -> int:
    # https://leetcode.com/discuss/general-discussion/786126/
    # ASSUMES THAT THERE IS A TRANSITION
    # MAY HAVE ISSUES AT THE EXTREMES

    def func(val):
        # if first True or last False, assume search space is in form
        # [False, ..., False, True, ..., True]

        # if first False or last True, assume search space is in form
        # [True, ..., True, False, ..., False]
        # for this case, func will now be negated
        if first ^ target:
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
    else:  # find last False
        return left - 1

grr = [g(x) for x in range(800)]
vrr = []

for power in range(2, 62):
    for i in range(1, 12):
        if g(2**power) > i:
            continue
        if g((2**(power+1) - 1)) < i:
            continue
        def func(x):
            return g(x) >= i
        idx = binary_search(func, left=2**power, right=2**(power+1) - 1)
        # print(power, i, idx)
        vrr.append((i, idx))

intervals = [(i, a, b-1) for (i,a),(j,b) in zip(vrr, vrr[1:])]
shortened = [[-1, -1, -1]]
for i,a,b in intervals:
    if i == shortened[-1][0]:
        shortened[-1][2] = b
    else:
        shortened.append([i,a,b])
shortened = shortened[1:]
for (i,a,b),(j,x,y) in zip(intervals, intervals[1:]):
    assert b + 1 == x
intervals = shortened
intervals[-1][2] = 10**18

# grr = [g(x) for x in range(800)]
    
# for i in range(3, 11):
#     def func(x):
#         return g(x) >= i
#     idx = binary_search(func, left=10, right=10**20)
#     assert g(idx) - 1 == i - 1
#     assert g(idx) == i
#     print(i, idx)

# intervals = [(i, a, b-1) for i,a,b in zip(range(2, 11), vrr, vrr[1:])]

intervals = [[2, 4, 7],
 [1, 8, 8],
 [2, 9, 728],
 [3, 729, 50624],
 [4, 50625, 4084100],
 [5, 4084101, 4194303],
 [4, 4194304, 5153631],
 [5, 5153632, 481890303],
 [6, 481890304, 536870911],
 [5, 536870912, 594823320],
 [6, 594823321, 64339296874],
 [7, 64339296875, 68719476735],
 [6, 68719476736, 78364164095],
 [7, 78364164096, 11688200277600],
 [8, 11688200277601, 1953124999999999],
 [9, 1953125000000000, 2251799813685247],
 [8, 2251799813685248, 2334165173090450],
 [9, 2334165173090451, 430804206899405823],
 [10, 430804206899405824, 2305843009213693951]]


def interval_overlap(x1, x2, y1, y2):
    # given intervals [x1,x2], [y1,y2]
    # [start, end] of overlapping interval
    # if start > end, there is no overlapping inteval
    return max(x1, y1), min(x2, y2)

# log(interval_overlap(8,8,1,10))


m9 = 10**9 + 7

def solve_(l, r):
    # your solution here

    res = 0

    for i,a,b in intervals:
        start, end = interval_overlap(a, b, l, r)
        if start > end:
            continue
        res += (end - start + 1)%m9 * i

    return res%m9


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
    l,r = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(l, r)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
