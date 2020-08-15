import sys
# import heapq, functools, collections
# import math, random
# from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

@njit((i8[:], i8, i8, i8), cache=True)
def solve(items,R,C,K):  # fix inputs here
    # console("----- solving ------")
    # console(R,C)

    grid = np.zeros((R, C), np.int64)

    for i in range(0, 3 * K, 3):
        x, y, v = items[i:i + 3]
        grid[x - 1, y - 1] = v

    # console(np.array(grid))  # PLEASE SILENCE
    # console("\n\n")

    dp = np.zeros((R, C, 4), np.int64)
    maxx = np.zeros((R, C), np.int64)

    if grid[0,0] > 0:
        dp[0][0][1] = dp[0][0][0] + grid[0][0]

    for i in range(1,R):
        dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1])
        if grid[i][0] > 0:
            dp[i][0][1] = dp[i][0][0] + grid[i][0]
        maxx[i][0] = max(dp[i][0])

    for j in range(1,C):
        for k in range(1,4):
            dp[0][j][k] = max(dp[0][j-1][k], dp[0][j-1][k-1] + grid[0][j])
        maxx[0][j] = max(dp[0][j])

    # console(np.array(dp)[:,:,0])  # PLEASE SILENCE
    # console(np.array(dp)[:,0,:])  # PLEASE SILENCE
    # console(np.array(dp)[0,:,:])  # PLEASE SILENCE
    # console(np.array(dp))  # PLEASE SILENCE
    # console("\n\nPost")

    for i in range(1,R):
        j_1 = 0
        for j in range(1,C):
            dp[i][j][0] = max(maxx[i-1][j], dp[i][j-1][0])
            if grid[i][j] > 0:
                dp[i][j][1] = max(dp[i][j-1][1], dp[i][j][0] + grid[i][j])
                for k in range(2,4):
                    dp[i][j][k] = max(dp[i][j-1][k], dp[i][j-1][k-1] + grid[i][j])
                j_1 = j
            else:
                for k in range(1,4):
                    dp[i][j][k] = dp[i][j-1][k]
            maxx[i][j] = max(dp[i][j])

    # console(np.array(dp)[:,:,0])  # PLEASE SILENCE
    # console(np.array(dp)[:,:,1])  # PLEASE SILENCE
    # console(np.array(dp)[:,:,2])  # PLEASE SILENCE
    # console(np.array(dp)[:,:,3])  # PLEASE SILENCE
    # console(np.array(dp))  # PLEASE SILENCE

    # return a string (i.e. not a list or matrix)
    return dp.max()


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H, W, K = map(int, readline().split())
XYV = np.array(read().split(), np.int64)
 
print(solve(XYV, H, W, K))
