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
a,b,c = list(map(int,input().split()))
k = int(input())

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer

cnt = 0

while b <= a:
    cnt += 1 
    b = b*2

while c <= b:
    cnt += 1 
    c = c*2

# print(cnt, a, b, c)

if cnt <= k:
    print("Yes")
else:
    print("No")
