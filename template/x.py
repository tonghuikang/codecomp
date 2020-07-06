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
 
if k%1000 == 0:
    print(0)
else:
    print(1000 - k%1000)