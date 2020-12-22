import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

@functools.lru_cache(maxsize=None)
def determine(arr, brr):
    arr = deque(arr)
    brr = deque(brr)
    while arr and brr:
        if arr[0] <= len(arr) and brr[0] <= len(brr):
            a_wins = determine(tuple(list(arr)[1:arr[0]]), tuple(list(brr)[1:brr[0]]))[0]               
            a = arr.popleft()
            b = brr.popleft()
            if a_wins:
                arr.append(a)
                arr.append(b)
            else:
                brr.append(b)
                brr.append(a)
        else:
            a = arr.popleft()
            b = brr.popleft()
            if a > b:
                arr.append(a)
                arr.append(b)
            if a < b:
                brr.append(b)
                brr.append(a)

    if len(arr) == 0:
        return False, brr
    return True, arr

def solve_(arr, brr):
    # arr = deque(arr)
    # brr = deque(brr)

    # while arr and brr:
    #     a = arr.popleft()
    #     b = brr.popleft()
    #     if a > b:
    #         arr.append(a)
    #         arr.append(b)
    #     if a < b:
    #         brr.append(b)
    #         brr.append(a)
    #     log(arr, brr)
    
    crr = determine(tuple(arr), tuple(brr))[1]
    log(crr)
    return sum([i*x for i,x in enumerate(list(crr)[::-1], start=1)])



def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]



def process(string_input):
    arr = [int(x.strip()) for x in string_input.strip().split("\n")]

    return arr


sample_input_1="""
9
2
6
3
1
"""

sample_input_2="""
5
8
4
7
10
"""

sample_input_1 = process(sample_input_1)
sample_input_2 = process(sample_input_2)

sample_res = solve(sample_input_1, sample_input_2)
print(sample_res)


test_input_1="""
31
24
5
33
7
12
30
22
48
14
16
26
18
45
4
42
25
20
46
21
40
38
34
17
50
"""

test_input_2="""
1
3
41
8
37
35
28
39
43
29
10
27
11
36
49
32
2
23
19
9
13
15
47
6
44
"""

test_input_1 = process(test_input_1)
test_input_2 = process(test_input_2)

test_res = solve(test_input_1, test_input_2)
print(test_res)



