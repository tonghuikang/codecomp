#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

# ---------------------------- template ends here ----------------------------

def query(a,b,c):
    query_string = "{} {} {}".format(a+1,b+1,c+1)
    print(query_string, flush=True)
    response = int(input())
    return response-1

def alert(pos):
    cout =  " ".join(str(x+1) for x in pos)
    print(cout, flush=True)
    response = int(input())
    assert response == 1

#   python interactive_runner.py python3 sample_local_testing_tool.py 0 -- python3 sample_interactive_script.py
#   python interactive_runner.py python3 sample_local_testing_tool.py 1 -- python3 sample_interactive_script.py
#   python interactive_runner.py python3 sample_local_testing_tool.py 2 -- python3 sample_interactive_script.py

# -----------------------------------------------------------------------------

# read one line and parse each word as an integer
t,n,q = list(map(int,input().split()))
assert n == 10

def check(permutation, queries, flag=False):
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                median = sorted([
                    (permutation[i],i),
                    (permutation[j],j),
                    (permutation[k],k)
                ])[1][1]
                if queries[i,j,k] != median:
                    return False
    return True


for _ in range(t):

    queries = {}
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                queries[i,j,k] = query(i,j,k)


    for permutation in itertools.permutations(range(n)):
        if check(permutation, queries):
            pinv = sorted(range(len(permutation)), key=permutation.__getitem__)
            break
    
    alert(pinv)
    # break


sys.exit()


# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here