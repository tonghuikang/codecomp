#!/usr/bin/env python3
import sys, getpass
import time
import itertools
from collections import Counter
start_time = time.time()
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

def tick():
    global start_time
    start_time = time.time()
def tock():
    log(time.time() - start_time)

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
    # log(_)
    # tick()
    queries = {}
    median_counter = Counter()
    for i in range(10):
        median_counter[i] = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                val = query(i,j,k)
                queries[i,j,k] = val
                median_counter[val] += 1

    permutation_ref = [k for k,v in median_counter.most_common()]
    permutation_ref = permutation_ref[::2][::-1] + permutation_ref[1::2]

    for pdt in itertools.product([0,1], repeat=n//2):
        permutation = [x for x in permutation_ref]
        for i,x in enumerate(pdt):
            if x:
                permutation[i], permutation[~i] = permutation[~i], permutation[i]
        pinv = sorted(range(len(permutation)), key=permutation.__getitem__)
        if check(pinv, queries):
            break
    # tock()

    alert(permutation)
    # break


sys.exit()


# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here