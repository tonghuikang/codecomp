import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def count(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    # i = len(a)
    count = 0
    base_count = 0
    length = len(str(a))

    for i in range(1,length):
        base_count += 5**(i)

    odd = True
    eligible = True
    for i,d in enumerate(str(a)):
        if odd:
            for j in "13579":
                if eligible and d == j and i == length - 1:
                    # console("add last")
                    count += 1 
                    break
                if d <= j:
                    break
                if eligible:
                    count += 5**(length - i - 1)
            if not d in "13579":
                eligible = False

        else:
            for j in "02468":
                if eligible and d == j and i == length - 1:
                    # console("add last")
                    count += 1 
                    break
                if d <= j:
                    break
                if eligible:
                    count += 5**(length - i - 1)
            if not d in "02468":
                eligible = False

        # console(i, d, count)
                
        odd = not odd

    # console("summ", a, base_count, count)
    return count + base_count


def solve_(a,b):
    # your solution here

    count = 0
    for i in range(a,b+1):
        # print(i)
        for x in str(i)[::2]:
            if not x in "13579":
                # print(x)
                break
        else:
            for x in str(i)[1::2]:
                if not x in "02468":
                    # print(x)
                    break
            else:
                count += 1
    return count

def solve_(a,b):
    return count(b) - count(a-1)

def console(*args):
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


ONLINE_JUDGE = False

# if Codeforces environment
if os.path.exists('input.txt'):
    ONLINE_JUDGE = True

if ONLINE_JUDGE:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass


def solve(*args):
    # screen input
    if not ONLINE_JUDGE:
        console("----- solving ------")
        console(*args)
        console("----- ------- ------")
    return solve_(*args)

# console(count(7))
# console("\n"*3)

# console(solve_(1,9))
# console(solve_(1,99)    - solve_(1,9))
# console(solve_(1,999)   - solve_(1,99))
# console(solve_(1,9999)  - solve_(1,999))
# console(solve_(1,99999) - solve_(1,9999))

# console(solve_(1,999)   - solve_(1,99))
# console(solve_(1000,1999))

# for a in range(1,10000):
#     ref = solve_(1,a)
#     pred = count(a)
#     console("x", a, ref, pred)
#     assert ref == pred

if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    a,b = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(a,b)  # please change
    
    # print result
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
    # print(*res)  # if printing a list