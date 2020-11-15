import sys, os
# import heapq, functools, collections
# import math, random
# from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

MOD = (10**9 + 7)

def solve_(grid, h, w):
    # your solution here

    dp = [[0 for _ in row] for row in grid]
    dp_hori = [[0 for _ in row] for row in grid]
    dp_vert = [[0 for _ in row] for row in grid]
    dp_diag = [[0 for _ in row] for row in grid]
    dp[0][0] = 1
    dp_vert[0][0] = 1
    dp_diag[0][0] = 1
    dp_hori[0][0] = 1

    for i,row in enumerate(grid[1:], start=1):
        if grid[i][0] == 1:
            continue
        dp[i][0] = dp_vert[i-1][0]
        dp_vert[i][0] = dp[i][0] + dp_vert[i-1][0]
        dp_diag[i][0] = dp[i][0]
        dp_hori[i][0] = dp[i][0]

    for j,cell in enumerate(grid[0][1:], start=1):
        if grid[0][j] == 1:
            continue
        dp[0][j] = dp_hori[0][j-1]
        dp_hori[0][j] = dp[0][j] + dp_hori[0][j-1]
        dp_diag[0][j] = dp[0][j]
        dp_vert[0][j] = dp[0][j]

    # console(dp)
    # console(dp_vert)
    # console(dp_hori)
    # console(dp_diag)
    # console("----")
    # console(dp_vert)
    # console(dp_vert[1-1][1])
    # console("-----")

    for i,row in enumerate(grid[1:], start=1):
        for j,cell in enumerate(row[1:], start=1):
            # console(i,j,dp_vert[i-1][j],dp_hori[i][j-1],dp_diag[i-1][j-1])
            if cell == 1:
                continue
            dp[i][j] = dp_vert[i-1][j] + dp_hori[i][j-1] + dp_diag[i-1][j-1]
            dp_vert[i][j] = (dp[i][j] + dp_vert[i-1][j])
            dp_hori[i][j] = (dp[i][j] + dp_hori[i][j-1])
            dp_diag[i][j] = (dp[i][j] + dp_diag[i-1][j-1])

            if i%5 == 0 or j%5 == 0:
                dp_vert[i][j] %= MOD
                dp_hori[i][j] %= MOD
                dp_diag[i][j] %= MOD

    # console(dp)
    # console(dp_vert)
    # console(dp_hori)
    # console(dp_diag)

    return dp[-1][-1]%MOD


def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


ONLINE_JUDGE = False

# if Codeforces environment
if os.path.exists('input.txt'):
    ONLINE_JUDGE = True

if ONLINE_JUDGE:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass


def solve(*args):
    # screen input
    # if not ONLINE_JUDGE:
    #     console("----- solving ------")
    #     console(*args)
    #     console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    h, w = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(h):
        grid.append([0 if chr(x) == '.' else 1 for x in input().strip()])

    res = solve(grid, h, w)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list