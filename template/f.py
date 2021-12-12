#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------

# https://atcoder.jp/contests/practice2/submissions/16616933
class LazySegmentTree():
    __slots__ = ["merge","merge_unit","operate","merge_operate","operate_unit","n","data","lazy"]
    def __init__(self,n,init,merge,merge_unit,operate,merge_operate,operate_unit):
        self.merge=merge
        self.merge_unit=merge_unit
        self.operate=operate
        self.merge_operate=merge_operate
        self.operate_unit=operate_unit

        self.n=(n-1).bit_length()
        self.data=[merge_unit for i in range(1<<(self.n+1))]
        self.lazy=[operate_unit for i in range(1<<(self.n+1))]
        if init:
            for i in range(n):
                self.data[2**self.n+i]=init[i]
            for i in range(2**self.n-1,0,-1):
                self.data[i]=self.merge(self.data[2*i],self.data[2*i+1])

    def propagate(self,v):
        ope = self.lazy[v]
        if ope == self.operate_unit:
            return
        self.lazy[v]=self.operate_unit
        self.data[(v<<1)]=self.operate(self.data[(v<<1)],ope)
        self.data[(v<<1)+1]=self.operate(self.data[(v<<1)+1],ope)
        self.lazy[v<<1]=self.merge_operate(self.lazy[(v<<1)],ope)
        self.lazy[(v<<1)+1]=self.merge_operate(self.lazy[(v<<1)+1],ope)

    def propagate_above(self,i):
        m=i.bit_length()-1
        for bit in range(m,0,-1):
            v=i>>bit
            self.propagate(v)

    def remerge_above(self,i):
        while i:
            c = self.merge(self.data[i],self.data[i^1])
            i>>=1
            self.data[i]=self.operate(c,self.lazy[i])

    def update(self,l,r,x):
        l+=1<<self.n
        r+=1<<self.n
        l0=l//(l&-l)
        r0=r//(r&-r)-1
        self.propagate_above(l0)
        self.propagate_above(r0)
        while l<r:
            if l&1:
                self.data[l]=self.operate(self.data[l],x)
                self.lazy[l]=self.merge_operate(self.lazy[l],x)
                l+=1
            if r&1:
                self.data[r-1]=self.operate(self.data[r-1],x)
                self.lazy[r-1]=self.merge_operate(self.lazy[r-1],x)
            l>>=1
            r>>=1
        self.remerge_above(l0)
        self.remerge_above(r0)

    def query(self,l,r):
        l+=1<<self.n
        r+=1<<self.n
        l0=l//(l&-l)
        r0=r//(r&-r)-1
        self.propagate_above(l0)
        self.propagate_above(r0)
        res=self.merge_unit
        while l<r:
            if l&1:
                res=self.merge(res,self.data[l])
                l+=1
            if r&1:
                res=self.merge(res,self.data[r-1])
            l>>=1
            r>>=1
        return res>>32

import sys

input = sys.stdin.buffer.readline

mod = 998244353
mask = 2**32 - 1

def merge(x,y):
    s = ((x>>32) + (y>>32)) % mod
    num = (x&mask) + (y&mask)
    return (s<<32) + num

merge_unit = 0

def operate(x,ope):
    s,num = x>>32,x&mask
    b,c = ope>>32,ope&mask
    s = (b*s + c*num) % mod
    return (s<<32)+num

def merge_operate(x,y):
    b1,c1 = x>>32,x&mask
    b2,c2 = y>>32,y&mask
    return (((b1*b2)%mod)<<32)+((b2*c1+c2)%mod)

operate_unit = 1<<32

# N,Q = map(int,input().split())
# a = list(map(int,input().split()))
# a = [(a[i]<<32)+1 for i in range(N)]

def solve_(arr):
    N = 10**9 + 7
    LST = LazySegmentTree(N,a,merge,merge_unit,operate,merge_operate,operate_unit)

for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 0:
        gomi,l,r,b,c = query
        LST.update(l,r,(b<<32)+c)
    else:
        gomi,l,r = query
        print(LST.query(l,r))



for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
