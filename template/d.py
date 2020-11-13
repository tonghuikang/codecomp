import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(lst):
    if len(lst) == 3:
        return [[0,1,2]]

    original = [x for x in lst]




    res = []
    while sum(lst) > 0:
        # if len(res) > len(lst):
        #     return -1

        number_of_odd = sum(x&1 for x in lst)

        if number_of_odd == 0 or number_of_odd == len(lst):
            lst = [x >> 1 for x in lst]
            # console("cont")
            continue
            

        count = [0 for _ in range(30)]
        for i in lst:
            for z in range(30):
                count[z] += i&1
                i = i >> 1
        ref = count.index(min([c if c%2 == 0 else len(lst) - c for c in count]))
        swap = 2**ref
        lst = [(x&swap) ^ ((x&1) << ref) ^ x for x in lst]


        # number of odd has to be even
        if len(lst)%2 == 0:
            if number_of_odd%2 != 0:
                return -1
            if number_of_odd < len(lst)//2:
                lst = [x^1 for x in lst]
        else:
            if number_of_odd%2 != 0:
                lst = [x^1 for x in lst]
        
        number_of_odd = sum(x&1 for x in lst)
        assert number_of_odd%2 == 0
        # console(lst, number_of_odd)

        fixing = []
        ref = 0
        for i,x in enumerate(lst):
            if x&1:
                fixing.append(i)
            else:
                ref = i
        
        for a,b in zip(fixing[::2],fixing[1::2]):
            new = lst[ref]^lst[a]^lst[b]
            lst[ref], lst[a], lst[b] = new, new, new
            res.append([ref,a,b])

            new = original[ref]^original[a]^original[b]
            original[ref], original[a], original[b] = new, new, new

        # console(lst)
        # console(original)
        lst = [x >> 1 for x in lst]
        # console(lst, res, fixing, number_of_odd)

    assert len(set(original)) == 1
    assert len(res) < len(lst)

    if len(res) > len(lst):
        return -1

    return res


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


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    k = int(input())
    
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

    res = solve(lst)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    if res == -1:
        print("NO")
        continue

    print("YES")
    print(len(res))
    for re in res:
        print(*[r+1 for r in re])

    # print("\n".join(cout))
    # print(*res)  # if printing a list