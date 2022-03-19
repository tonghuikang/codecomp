#!/usr/bin/env python3
import sys
import networkx as nx
from collections import deque
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
import getpass  # not available on codechef
OFFLINE_TEST = getpass.getuser() == "htong"
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


# ---------------------------- template ends here ----------------------------


def sliding_window_maximum(nums, k):
    # leetcode.com/problems/sliding-window-maximum/discuss/65901
    # log("sliding_window_maximum", nums, k)
    deq, n, ans = deque([0]), len(nums), []
    for i in range(n):
        while deq and deq[0] <= i - k:
            deq.popleft()
        while deq and nums[i] >= nums[deq[-1]] :
            deq.pop()
        deq.append(i)
        ans.append(nums[deq[0]])

    log(ans)
    # return ans[k-1:]
    return [ans[k-1]]*(k//2) + ans[k-1:] + [ans[-1]]*(k//2)


LARGE = 10**16

def solve_(mrr,n,m,d):
    # your solution here

    def gen_arr(a):
        a -= 1
        return [-LARGE]*n + [-abs(a-i) for i in range(n)] + [-LARGE]*n
        
    res = 0
    a0, b0, t0 = mrr[0]
    dp = gen_arr(a0)
    res = b0
    prev_t = t0

    for a,b,t in mrr[1:]:
        log(a,b,t)
        res += b
        t_diff = t - prev_t
        dist = t_diff * d
        window_size = 2*dist + 1

        # log(len(dp), dp, window_size)

        window_size = min(2*n-1, window_size)
        dp = sliding_window_maximum(dp, window_size)

        log(len(dp), dp, window_size)

        new_dp = gen_arr(a)

        assert len(dp) == len(new_dp)

        dp = [a+b for a,b in zip(dp, new_dp)]
        prev_t = t

    return res + max(dp)


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,m,d = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(m)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr,n,m,d)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
