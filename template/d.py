#!/usr/bin/env python3
import sys

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

e18 = 10**18 + 10

# ---------------------------- template ends here ----------------------------


LARGE = e18

def solve_(arr):
    # your solution here

    # fix-forward, no-fix-forward
    dp = [[LARGE, LARGE], [0, 0]]

    for x in arr:
        if x == 0:
            dp = [[LARGE, LARGE], min(dp)]
            continue

        new_dp = [[LARGE, LARGE], [LARGE, LARGE]]

        # fix the current step with fix-forward
        new_dp[1] = min(new_dp[1], [dp[0][0], dp[0][1] + 2 * x])

        # fix the current step with no fix-forward
        new_dp[1] = min(new_dp[1], [dp[1][0] + 1, dp[1][1] + x])
        
        # fix-forward the current step
        new_dp[0] = min(new_dp[0], [dp[1][0] + 1, dp[1][1] + 2 * x])

        dp = new_dp

        # log(dp)

    return dp[1][-1]


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

    res = solve_(arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
