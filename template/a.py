import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict



lst = []

for case_num in range(int(input())):
    # read line as a string
    lst.append(input())

    
c = Counter(lst)


print("AC x {}".format(c["AC"]))
print("WA x {}".format(c["WA"]))
print("TLE x {}".format(c["TLE"]))
print("RE x {}".format(c["RE"]))


