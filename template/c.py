import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

@functools.lru_cache(maxsize=None)
def invmod(a,b):
    return 0 if a==0 else 1 if b%a==0 else b - invmod(b%a,a)*b//a

def solve(lst):  # fix inputs here
    console("----- solving ------")
    if len(lst) == 1:
        print("1 1")
        print(0)
        print("1 1")
        print(0)
        print("1 1")
        print(-lst[0])
        return

    length = len(lst)

    inv = invmod(length, length-1)
    console(inv)

    arr = [x*(length-1) for x in lst[1:]]
    console(arr)

    print("{} {}".format(2, length))    
    print(" ".join(str(x) for x in arr))
    
    lst[1:] = [a+b for a,b in zip(arr, lst[1:])]

    diff = lst[0]%len(lst)

    if diff == 0:
        print("1 1")
        print(0)
    
    else:
        print("{} {}".format(1, diff))
        print("{} ".format(-diff) + " ".join(["0" for i in range(diff-1)]))

    lst[0] = lst[0] - diff

    assert all(x%length == 0 for x in lst)

    print("{} {}".format(1, length))
    print(" ".join([str(-x) for x in lst])) 

    return


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for _ in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    _ = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    solve(lst)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
