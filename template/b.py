#!/usr/bin/env python3
import sys
from collections import deque

input = sys.stdin.readline  # to read input quickly


# ---------------------------- template ends here ----------------------------

val = 2**32

def decode(z):
    return divmod(z, val)
    
def encode(x,y):
    return x * val + y

def solve(a,b,c,d,m):
    # your solution here

    # hypothesis - you can't go anywhere

    dist = {}
    dist[encode(a,b)] = 0

    queue = deque([(a,b)])

    while queue:
        x,y = queue.popleft()
        cnt = dist[encode(x,y)]

        xx, yy = x&y, y

        if encode(xx,yy) not in dist:
            queue.append((xx,yy))
            dist[encode(xx,yy)] = cnt + 1

        xx, yy = x|y, y

        if encode(xx,yy) not in dist:
            queue.append((xx,yy))
            dist[encode(xx,yy)] = cnt + 1

        xx, yy = x,x^y

        if encode(xx,yy) not in dist:
            queue.append((xx,yy))
            dist[encode(xx,yy)] = cnt + 1

        xx, yy = x,y^m

        if encode(xx,yy) not in dist:
            queue.append((xx,yy))
            dist[encode(xx,yy)] = cnt + 1

    if encode(c,d) in dist:
        return dist[encode(c,d)]

    # log(len(dist))
    
    return -1


# solve(2**30-1,0,4512312,123123,1)

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    a,b,c,d,m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(a,b,c,d,m)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
