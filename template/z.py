## for use in beginner level questions where speed is key
## and also for single test case code
## mastercopy for x,y,z

import sys
import heapq, functools, collections
import random
from collections import Counter, defaultdict

# read line as a string
# strr = input()

# read line as an integer
k = int(input())

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# arr = list(map(int,input().split()))

if k == 1:
    print(0)
    sys.exit()

# if k == 2:
#     print(2)
#     sys.exit()

res = 0
MOD = 10**9 + 7

have_all = pow(10,k,MOD)
dont_have_0 = pow(9,k,MOD)
dont_have_9 = pow(9,k,MOD)
dont_have_09 = pow(8,k,MOD)

print((have_all - dont_have_0 - dont_have_9 + dont_have_09) % MOD)
