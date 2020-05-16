import sys
import heapq
import random
import collections

# not available on Codeforces, available on Google
# import numpy as np 
# import scipy

def solve():  # fix inputs here
    def console(*args):
        # the judge will not read this print statement
        print(args, file=sys.stderr)
    console("solving")

    # return a string (i.e. not a list or matrix)
    return ""  


for case_num in range(int(input())):
    # read one integer
    k = int(input()) 
    
    # read one list and parse as integers
    lst = list(map(int,input().split()))

    # read matrix and parse as integers
    lst = list(map(int,input().split()))
    nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve()  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
