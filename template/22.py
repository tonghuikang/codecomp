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
    cache = {}
    # log(arr, brr)
    arr = list(arr)
    brr = list(brr)
    while arr and brr:
        if (tuple(arr), tuple(brr)) in cache:
        #     # a = arr[0]
        #     # b = brr[0]
        #     # arr.append(a)
        #     # arr.append(b)
            log("cached", arr, brr)
            return True, arr
        
        atup = tuple(arr)
        btup = tuple(brr)

        if arr[0] <= len(arr)-1 and brr[0] <= len(brr)-1:
            a_wins = determine(tuple(arr)[1:arr[0]+1], tuple(brr)[1:brr[0]+1])[0]               
            a = arr[0]
            b = brr[0]

            # if (tuple(arr), tuple(brr)) in cache:
            #     awins = True

            del arr[0]
            del brr[0]

            if a_wins:
                arr.append(a)
                arr.append(b)
                cache[atup, btup] = (True, arr)
            else:
                brr.append(b)
                brr.append(a)
                cache[atup, btup] = (False, brr)
        else:
            a = arr[0]
            b = brr[0]

            awins = False
            # if (tuple(arr), tuple(brr)) in cache:
            #     awins = True

            del arr[0]
            del brr[0]
            if a > b or awins:
                arr.append(a)
                arr.append(b)
                cache[atup, btup] = (True, arr)
            if a < b:
                brr.append(b)
                brr.append(a)
                cache[atup, btup] = (False, brr)

    if len(arr) == 0:
        # cache[tuple(arr), tuple(brr)] = False, brr
        return False, brr

    # cache[tuple(arr), tuple(brr)] = True, arr
    return True, arr

def solve_(arr, brr):
    # arr, brr = brr, arr
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
43
19
"""

sample_input_2="""
2
29
14
"""

sample_input_1 = process(sample_input_1)
sample_input_2 = process(sample_input_2)

sample_res = solve(sample_input_1, sample_input_2)
print(sample_res)


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



