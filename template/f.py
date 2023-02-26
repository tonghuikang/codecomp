#!/usr/bin/env python3
import sys
import itertools
from collections import Counter
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}

# if testing locally, print to terminal with a different color
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
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


def longest_common_subsequence(arr, brr):
    # leetcode.com/problems/longest-common-subsequence/discuss/351689/
    m, n = map(len, (arr, brr))
    if m < n:
        return longest_common_subsequence(brr, arr)
    dp = [0] * (n + 1)
    for c in arr:
        prevRow, prevRowPrevCol = 0, 0
        for j, d in enumerate(brr):
            prevRow, prevRowPrevCol = dp[j + 1], prevRow
            dp[j + 1] = prevRowPrevCol + 1 if c == d else max(dp[j], prevRow)
    return dp[-1]


def lcs3(a, b, c):
    # https://stackoverflow.com/questions/5057243/longest-common-subsequence-of-3-strings
    m = len(a)
    l = len(b)
    n = len(c)
    subs = [[[0 for k in range(n+1)] for j in range(l+1)] for i in range(m+1)]

    for i, x in enumerate(a):
        for j, y in enumerate(b):
            for k, z in enumerate(c):
                if x == y and y == z:
                    subs[i+1][j+1][k+1] = subs[i][j][k] + 1
                else:
                    subs[i+1][j+1][k+1] = max(subs[i+1][j+1][k], 
                                              subs[i][j+1][k+1], 
                                              subs[i+1][j][k+1])
    # return subs[-1][-1][-1] #if you only need the length of the lcs
    lcs = 0
    while m > 0 and l > 0 and n > 0:
        step = subs[m][l][n]
        if step == subs[m-1][l][n]:
            m -= 1
        elif step == subs[m][l-1][n]:
            l -= 1
        elif step == subs[m][l][n-1]:
            n -= 1
        else:
            lcs += 1
            m -= 1
            l -= 1
            n -= 1

    return lcs

# def lcs3(X,Y,Z):
#     # X = "AGGT12"
#     # Y = "12TXAYB"
#     # Z = "12XBA"
    
#     # Returns length of LCS for
#     # X[0..m-1], Y[0..n-1] and Z[0..o-1]
#     def lcsOf3(i, j, k) :
    
#         if(i == -1 or j == -1 or k == -1) :
#             return 0
            
#         if(dp[i][j][k] != -1) :
#             return dp[i][j][k]
        
#         if(X[i] == Y[j] and Y[j] == Z[k]) :
#             dp[i][j][k] = 1 + lcsOf3(i - 1,
#                                     j - 1, k - 1)
#             return dp[i][j][k]
            
#         else :
#             dp[i][j][k] = max(max(lcsOf3(i - 1, j, k),
#                                 lcsOf3(i, j - 1, k)),
#                                 lcsOf3(i, j, k - 1))
            
#             return dp[i][j][k]
    
#     m = len(X)
#     n = len(Y)
#     o = len(Z)

#     dp = [[[-1 for i in range(o+1)]
#             for j in range(n+1)]
#             for k in range(m+1)]

#     return(lcsOf3(m - 1, n - 1, o - 1))


def solve_(arr):
    # your solution here
    c = Counter(arr)

    log(c)

    res = 0

    for num_repeat in range(2, 8):
        if num_repeat == 4:
            # if can repeat 4, it can repeat 2
            continue

        brr = []
        for x in arr:
            if c[x] < num_repeat:
                continue
            brr.append(x)
        if not brr:
            continue

        n = len(brr)

        if num_repeat == 2:
            for i in range(1, n):
                val = longest_common_subsequence(brr[:i], brr[i:])
                # log(val)
                res = max(res, val * num_repeat)

        log(res)

        if num_repeat == 3:
            for a,b in itertools.combinations(list(range(1,n)), 2):
                val = lcs3(brr[:a], brr[a:b], brr[b:])
                res = max(res, val * num_repeat)

        log(res)

        if num_repeat == 4:
            continue

        if num_repeat == 6:
            continue

        if num_repeat != 5:
            continue

        def count_seq(perm):
            n = len(perm)
            ptr = 0
            cnt = 0
            for x in brr:
                if x == perm[ptr]:
                    ptr += 1
                if ptr == n:
                    ptr = 0
                    cnt += 1
            # log(perm, cnt)
            return cnt

        # log(brr)

        idxs = [len(brr) // 5] * 5
        remainder = n - sum(idxs)
        for ptr in range(5):
            if remainder:
                idxs[ptr] += 1
                remainder -= 1
        
        sections = []
        psum = [0]

        for idx in idxs:
            psum.append(psum[-1] + idx)

        # log(psum)

        allset = set()

        for a,b in zip(psum, psum[1:]):
            # log(a,b)
            qrr = brr[a:b]
            # log(qrr)
            for prod in itertools.product([0,1], repeat=len(qrr)):
                query = []
                for a,b in zip(prod, qrr):
                    if a:
                        query.append(b)
                allset.add(tuple(query))
        
        # log(brr)
        # log(allset)

        for seq in allset:
            if not seq:
                continue
            val = count_seq(seq)
            # log(seq, val)
            res = max(res, val*len(seq))

    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    srr = input().strip()
    arr = [abc_map[x] for x in srr]

    log(len(srr))

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
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
