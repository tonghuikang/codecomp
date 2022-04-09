# command to run
# python interactive_runner.py python3 interactive_google_local_testing_tool.py -- python3 interactive_google.py

# you need to download interactive_runner.py from
# https://storage.googleapis.com/coding-competitions.appspot.com/interactive_runner.py
# this is question agnostic

# you need to download interactive_google_local_testing_tool.py from the question page
# copy the testing tool code downloaded from the question page to the file
# this is question specific
# for some testing tools you might need to specify the test case and it will look something like
# python interactive_runner.py python3 interactive_google_local_testing_tool.py 0 -- python3 interactive_google.py

# interactive_google.py is the solution that you write, which is this file
# please remember to flush output
# run sys.exit() at the end as well


import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "htong"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

# ---------------------------- template ends here ----------------------------

def print_array(lst):
    print(*lst, flush=True)
    return None

def teleport(pos):
    print("T {}".format(pos+1), flush=True)
    response = list(map(int,input().split()))
    return response

def alert(pos):
    print("E {}".format(pos), flush=True)

# -----------------------------------------------------------------------------

# read line as an integer
# k = int(input())

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = v
# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here

for case_num in range(int(input())):
    n = int(input())

    diff = [2**x // 2 for x in range(1,29)]
    pos = [diff*4+1+diff for diff in diff]
    neg = [diff*4+1 for diff in diff]

    # pos.append(1+2**28)
    # neg.append(1)
    # pos.append(2+2**29)
    # neg.append(2)

    # log(pos)
    # log(neg)
    # log(diff)
    # break

    for a,b,c in zip(pos, neg, diff):
        assert a == b+c
        # no diff   - a   | b,c
        # make diff - a,c | b

    drr = diff + pos + neg
    # log(sum(drr))
    assert len(drr) == len(set(drr))
    
    arrlen = 100 - len(drr)
    # log(arrlen)
    arr = []
    for x in range(29,-1,-1):
        if len(arr) == arrlen:
            break
        if x not in drr:
            arr.append(2**x + 10)
    else:
        assert False

    orr = drr+arr
    # log(orr)
    # orr = orr[:100]
    # log(orr)
    print_array(orr)
    
    brr = list(map(int,input().split()))

    bin1 = []
    bin2 = []
    sum1 = 0
    sum2 = 0

    all_nums = orr+brr
    # log(sum(all_nums))
    target_sum = sum(all_nums) // 2

    xrr = brr+arr
    xrr.sort()
    xrr.reverse()

    # log(xrr)

    for x in xrr:
        if sum1 < sum2:
            bin1.append(x)
            sum1 += x
        else:
            bin2.append(x)
            sum2 += x

    if sum1 > sum2:
        sum1, sum2 = sum2, sum1
        bin1, bin2 = bin2, bin1
    target_diff = sum2 - sum1

    # log(target_diff)
    # assert target_diff%2 == 0

    binrr = (bin(target_diff)[2:]).zfill(30)[::-1]
    # log(binrr)

    for a,b,c,x in zip(pos, neg, diff, binrr[1:]):
        assert a == b+c
        if x == "1":
            # make diff
            bin1.append(a)
            bin1.append(c)

            bin2.append(b)
        else:
            bin1.append(a)

            bin2.append(c)
            bin2.append(b)
        
        # log(sum(bin2) - sum(bin1))

    # log(target_sum, sum(bin1))
    # assert target_sum == sum(bin1)
    # for x in bin1:
    #     assert x in all_nums, x

    assert sum(bin2) - sum(bin1) == 0

    # log(sum(bin2) - sum(bin1))
    print_array(bin1)
    

sys.exit()
