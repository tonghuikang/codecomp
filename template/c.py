import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid):  # fix inputs here

    console("----- solving ------")
    baseline = sum(b for a,b,c in grid)

    # pos = [a for a,b,c in grid]
    # diff = [c-b for a,b,c in grid] 
    
    char = [(a-1,c-b) for a,b,c in grid]
    char = sorted(char, key=lambda x: abs(x[1]))[::-1]

    console(baseline)
    console(char)
    console('=')

    assignment = [None for _ in char]
    right_pointer = [None for _ in char]
    left_pointer = [None for _ in char]
    discard = 0 
    for pos,diff in char:
        if assignment[pos] == None:
            assignment[pos] = max(0,diff)

        visited = [pos]
        if diff > 0:
            while pos > 0:
                if assignment[pos] == None:
                    if left_pointer[pos] == None:
                        pos -= 1
                    else:
                        visited.append(pos)
                        pos = left_pointer[pos]
                else:
                    for idx in visited:
                        left_pointer[idx] = pos-1
                    assignment[pos] = max(0,diff)
                    break
            if pos < 0:
                discard += min(0,diff)

        if diff < 0:
            pos = pos+1
            while pos < len(char):
                if assignment[pos] == None:
                    if right_pointer[pos] == None:
                        pos -= 1
                    else:
                        visited.append(pos)
                        pos = right_pointer[pos]
                else:
                    for idx in visited:
                        right_pointer[idx] = pos
                    assignment[pos] = max(0,diff)
                    break
            if pos < 0:
                discard += min(0,diff)

        if diff == 0:
            break
        
    console("res")
    console(assignment)
    console(left_pointer)
    console(right_pointer) 
    console(discard)   
    assignment = [x for x in assignment if x != None]
    
    return baseline + sum(assignment) - discard


    

    # return a string (i.e. not a list or matrix)
    return baseline


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    nrows = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve(grid)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
