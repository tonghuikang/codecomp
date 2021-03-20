#!/usr/bin/env python3
import sys, getpass
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
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

# ---------------------------- template ends here ----------------------------

# FFT convolution
# https://atcoder.jp/contests/abc196/submissions/21089133
ROOT = 3
MOD = 998244353
roots  = [pow(ROOT,(MOD-1)>>i,MOD) for i in range(24)] # 1 の 2^i 乗根
iroots = [pow(x,MOD-2,MOD) for x in roots] # 1 の 2^i 乗根の逆元

def untt(a,n):
    for i in range(n):
        m = 1<<(n-i-1)
        for s in range(1<<i):
            w_N = 1
            s *= m*2
            for p in range(m):
                a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m])%MOD, (a[s+p]-a[s+p+m])*w_N%MOD
                w_N = w_N*roots[n-i]%MOD
 
def iuntt(a,n):
    for i in range(n):
        m = 1<<i
        for s in range(1<<(n-i-1)):
            w_N = 1
            s *= m*2
            for p in range(m):
                a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m]*w_N)%MOD, (a[s+p]-a[s+p+m]*w_N)%MOD
                w_N = w_N*iroots[i+1]%MOD
            
    inv = pow((MOD+1)//2,n,MOD)
    for i in range(1<<n):
        a[i] = a[i]*inv%MOD
 
def convolution(a,b):
    la = len(a)
    lb = len(b)
    if min(la, lb) <= 50:
        if la < lb:
            la,lb = lb,la
            a,b = b,a
        res = [0]*(la+lb-1)
        for i in range(la):
            for j in range(lb):
                res[i+j] += a[i]*b[j]
                res[i+j] %= MOD
        return res
 
    deg = la+lb-2
    n = deg.bit_length()
    N = 1<<n
    a += [0]*(N-len(a))
    b += [0]*(N-len(b))
    untt(a,n)
    untt(b,n)
    for i in range(N):
      a[i] = a[i]*b[i]%MOD
    iuntt(a,n)
    return a[:deg+1]


def solve_(arr, brr):

    lbrr = len(brr)
    arr = [1-2*int(x) for x in arr]
    brr = [1-2*int(x) for x in brr] + [0]*(len(arr)-len(brr))

    half = 10**8
    crr = convolution(arr[::-1], brr)
    crr = [x-MOD if x > half else x for x in crr]

    prefix = lbrr - 1
    expected = len(arr) - lbrr + 1
    relevant = crr[prefix:expected+prefix]

    best = max(relevant)

    return int(round((lbrr-best)/2))


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    arr = input().strip()
    brr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(arr, brr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)