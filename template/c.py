from functools import lru_cache
from itertools import cycle
import math
import random

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


def explore(start, matrix):
    grid = [[cell - (start + i + j) for j,cell in enumerate(row)]
            for i,row in enumerate(matrix)]
    
    invalid = False
    for i,row in enumerate(grid):
        for j,cell in enumerate(row):
            if cell < 0:
                invalid = True

    if invalid:
        return 10**16 + start
    
    res = minPathSum(grid)
    return res


def solve(matrix):
    upper = matrix[0][0]
    lower = -30
    middle = (upper + lower)// 2

    upper_val = explore(upper, matrix)
    lower_val = explore(lower, matrix)

    res = min(upper_val, lower_val)

    # for i in range(lower, upper):
    #     print(explore(i, matrix))

    for _ in range(51):
        # print(middle)
        middle = (upper + lower)// 2
        middle_upper_val = explore((middle+upper)//2, matrix)
        middle_val = explore(middle, matrix)
        middle_lower_val = explore((middle+lower)//2, matrix)
        
        res = min(res, middle_upper_val, middle_val, middle_lower_val)
        if middle_lower_val <= middle_upper_val:
            upper = middle
        else:
            lower = middle
    
    r1 = explore(middle+2, matrix)
    r2 = explore(middle+1, matrix)
    r3 = explore(middle, matrix)
    r4 = explore(middle-1, matrix)
    r5 = explore(middle-2, matrix)

    return min(res,r1,r2,r3,r4,r5)

for _ in range(int(input())):
    nrows, _ = list(map(int,input().split()))
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))
    print(solve(grid))
    # print()
    # print()   
    # print()
    # print() 
