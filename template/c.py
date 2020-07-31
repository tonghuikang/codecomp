#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'treeConstruction' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. LONG_INTEGER X
#

def treeConstruction(N, X):
    if N == 1:
        if X == 0:
            return []
        else:
            return [[-1, -1]]
    if X < N-1:
        return [[-1, -1]]
    if X > ((N-1)*N)//2:
        return [[-1, -1]]

    # distributable
    
    flood = ((N)*(N-1))//2
    fill = X
    
    missing = flood - fill
    
    guess = int(math.sqrt(missing))
    guesses = [guess-1, guess, guess+1, guess+2]
    
    # print(guesses)
    
    for guess in guesses:
        if guess >= 0 and (guess*(guess+1))//2 >= missing:
            break
            
    height = N-guess-1
    if X == N-1:
        height = 1
    if X == (N*(N-1))//2:
        height = N-1
        
    print("flood", flood)
    print("fill", fill)
    print("guess", guess)
    
    # above code is to obtain the height
    print("height", height)
        
    res = []
    for i in range(height):
        # print("main")
        res.append([i+1, i+2])
    
    remaining_nodes = N - height - 1
    remaining_score = fill - (height*(height+1)//2) - remaining_nodes
    
    print("remaining_nodes", remaining_nodes)
    print("remaining_score", remaining_score)
    print()
    
    for i in range(height, N-1):
        assign = min(remaining_score, height)
        remaining_score = remaining_score - (assign)
        res.append([assign+1, i+2])
                
            
    res = [[min(N, max(1, x)), min(N, max(1, y))] for x,y in res]
    # print(res)
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        first_multiple_input = input().rstrip().split()

        N = int(first_multiple_input[0])

        X = int(first_multiple_input[1])

        result = treeConstruction(N, X)

        fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
        fptr.write('\n')

    fptr.close()