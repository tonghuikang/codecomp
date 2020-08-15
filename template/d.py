import sys
# import heapq, functools, collections
# import math, random
# from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(items,R,C):  # fix inputs here
    console("----- solving ------")
    console(R,C)

    grid = [[0 for _ in range(C)] for _ in range(R)]

    for r,c,v in items:
        grid[r-1][c-1] = v

    # console(np.array(grid))  # PLEASE SILENCE
    console("\n\n")

    dp = [[[0 for _ in range(4)] for _ in range(C)] for _ in range(R)]

    if grid[0][0] > 0:
        dp[0][0][1] = dp[0][0][0] + grid[0][0]

    for i in range(1,R):
        dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1])
        if grid[i][0] > 0:
            dp[i][0][1] = dp[i][0][0] + grid[i][0]

    for j in range(1,C):
        for k in range(1,4):
            dp[0][j][k] = max(dp[0][j-1][k], dp[0][j-1][k-1] + grid[0][j])

    # console(np.array(dp)[:,:,0])  # PLEASE SILENCE
    # console(np.array(dp)[:,0,:])  # PLEASE SILENCE
    # console(np.array(dp)[0,:,:])  # PLEASE SILENCE
    # console(np.array(dp))  # PLEASE SILENCE
    # console("\n\nPost")

    for i in range(1,R):
        for j in range(1,C):
            dp[i][j][0] = max(max(dp[i-1][j][k] for k in range(4)), dp[i][j-1][0])
            if grid[i][j] > 0:
                dp[i][j][1] = max(dp[i][j-1][1], dp[i][j][0] + grid[i][j])
                for k in range(2,4):
                    dp[i][j][k] = max(dp[i][j-1][k], dp[i][j-1][k-1] + grid[i][j])
            else:
                for k in range(1,4):
                    dp[i][j][k] = dp[i][j-1][k]

    # console(np.array(dp)[:,:,0])  # PLEASE SILENCE
    # console(np.array(dp)[:,:,1])  # PLEASE SILENCE
    # console(np.array(dp)[:,:,2])  # PLEASE SILENCE
    # console(np.array(dp)[:,:,3])  # PLEASE SILENCE
    # console(np.array(dp))  # PLEASE SILENCE

    # return a string (i.e. not a list or matrix)
    return max(dp[R-1][C-1][k] for k in range(4))


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
inn = sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    r,c,nrows = list(map(int,inn[0].split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for t in range(1,nrows+1):
        grid.append(list(map(int,inn[t].split())))

    res = solve(grid,r,c)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
