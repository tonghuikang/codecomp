from functools import lru_cache
from itertools import cycle
import math
import random

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def solve(lst):
    if len(lst) == 2:
        return lcm(*lst)

    if len(lst) == 3:
        return math.gcd(
            math.gcd(
                lcm(lst[0], lst[1]), 
                lcm(lst[1], lst[2])),
            lcm(lst[0], lst[2])
        )

    # random.shuffle(lst)
    # lst = sorted(lst)

    root = 1
    # root = math.gcd(lst[0], lst[1])
    # for i in lst:
    #     root = math.gcd(root, i)
    # lst = [x//root for x in lst]
    # print(root, lst)

    lcm_arr = set()
    for a,b in zip(lst[1:] + [lst[0]], [lst[-1]] + lst[:-1]):
        lcm_arr.add(lcm(a, b))

    for _ in range(3000000//len(lst)): 
        # print(i)
        random.shuffle(lst)
        for a,b in zip(lst[1:], lst[:-1]):
            lcm_arr.add(lcm(a, b))

    # print(sorted(set(lcm_arr)))
    lcm_arr = list(lcm_arr)
    res = math.gcd(lcm_arr[0], lcm_arr[1])
    for lcm_element in lcm_arr:
        res = math.gcd(res, lcm_element)

    return res*root

_ = input()
lst = list(map(int,input().split()))
print(solve(lst))
