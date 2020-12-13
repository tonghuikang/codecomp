import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


# Python implementation of Binary Indexed Tree 
  
# Returns sum of arr[0..index]. This function assumes 
# that the array is preprocessed and partial sums of 
# array elements are stored in BITree[]. 
def getsum(BITTree,i): 
    s = 0 # initialize result 
  
    # index in BITree[] is 1 more than the index in arr[] 
    i = i+1
  
    # Traverse ancestors of BITree[index] 
    while i > 0: 
  
        # Add current element of BITree to sum 
        s ^= BITTree[i] 
  
        # Move index to parent node in getSum View 
        i -= i & (-i) 
    return s
  

# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and 
# all of its ancestors in tree. 
def updatebit(BITTree , n , i ,v): 
  
    # index in BITree[] is 1 more than the index in arr[] 
    i += 1
  
    # Traverse all ancestors and add 'val' 
    while i <= n: 
  
        # Add 'val' to current node of BI Tree 
        BITTree[i] ^= v 
  
        # Update index to that of parent in update View 
        i += i & (-i) 
  
  
# Constructs and returns a Binary Indexed Tree for given 
# array of size n. 
def construct(arr, n): 
  
    # Create and initialize BITree[] as 0 
    BITTree = [0]*(n+1)
  
    # Store the actual values in BITree[] using update() 
    for i in range(n): 
        updatebit(BITTree, n, i, arr[i]) 
  
    # Uncomment below lines to see contents of BITree[] 
    #for i in range(1,n+1): 
    #     print BITTree[i], 
    return BITTree 
  
  

def solve_(lst, grid):
    # your solution here
    freq = [0] + lst
    BITTree = construct(freq,len(freq)) 

    for a,b,c in grid:
        if a == 2:
            print(getsum(BITTree,b-1) ^ getsum(BITTree,c))
        
        if a == 1:
            (updatebit(BITTree, len(freq), b, c))



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

for _ in [1]:
# for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    _, nrows = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve(lst, grid)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
    # print(*res)  # if printing a list