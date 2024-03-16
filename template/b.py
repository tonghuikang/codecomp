#!/usr/bin/env python3
import sys
import random

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass

    OFFLINE_TEST = getpass.getuser() == "htong"


def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x - 1 for x in arr]


def minus_one_matrix(mrr):
    return [[x - 1 for x in row] for row in mrr]


# ---------------------------- template ends here ----------------------------


def manachers(S):
    # https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/discuss/1389421/
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/suffix_array.py
    # https://cp-algorithms.com/string/suffix-array.html
    A = "@#" + "#".join(S) + "#$"
    Z = [0] * len(A)
    center = right = 0
    for i in range(1, len(A) - 1):
        if i < right:
            Z[i] = min(right - i, Z[2 * center - i])
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
            Z[i] += 1
        if i + Z[i] > right:
            center, right = i, i + Z[i]
    return Z[2:-2:2]


def solve_(srr, qrr):
    # n = len(srr)
    # your solution here

    # all equal - no good
    # ababababa - odd no good, even good
    # full palindrome?

    # log()
    mrr = manachers(srr)
    mrr2 = manachers("#".join(srr))
    # log(mrr)
    # log(mrr2)
    # log()

    arr = [abc_map[x] for x in srr]

    cur_cnt = [0 for _ in range(26)]
    cntrs = [[0 for _ in range(26)]]

    for x in arr:
        cur_cnt[x] += 1
        cntrs.append([x for x in cur_cnt])

    res = []

    for l,r in qrr:
        l -= 1
        cntr = [x-y for x,y in zip(cntrs[r], cntrs[l])]
        log(cntr)

        # if all same
        if cntr.count(0) == 25:
            res.append(0)
            continue

        n = r-l
        n2 = n // 2
        if (l+r)%2 == 1:  # odd length
            # check if the whole thing is a palindrome
            is_entire_substring_palindrome = False
            if mrr[(r+l) // 2] >= n:
                is_entire_substring_palindrome = True

            if is_entire_substring_palindrome:
                # check if alternating
                if mrr[(r+l) // 2 + 1] >= n-2 and mrr[(r+l) // 2 - 1] >= n-2:
                    log("z")
                    val = n2 * (n2+1)
                    # sum of all even numbers
                else:
                    log("a")
                    val = n*(n-1) // 2 - 1
                    # sum of all numbers except 1 and length
            else:
                log("c")
                val = n*(n+1) // 2 - 1
                # sum of all numbers except 1

            res.append(val)

        else:
            # check if palindrome
            is_entire_substring_palindrome = False
            if mrr2[r+l-1] >= n*2-1:
                is_entire_substring_palindrome = True

            log(is_entire_substring_palindrome, mrr2[r+l-1], r, l)

            if is_entire_substring_palindrome:
                log("f")
                val = n*(n-1) // 2 - 1
            else:
                # check if alternating
                if mrr[(r+l) // 2 - 1] >= n-1 and mrr[(r+l) // 2] >= n-1:
                    log("d")
                    val = 2 * n2 * (n2+1) // 2
                    # sum of all even numbers
                else:
                    log("e")
                    val = n*(n+1) // 2 - 1
                    # sum of all numbers except 1

            res.append(val)

    return res


def is_palindrome(s):
    return s == s[::-1]

def f(s):
    n = len(s)
    result = 0
    for k in range(2, n+1):
        for i in range(n-k+1):
            substring = s[i:i+k]
            if not is_palindrome(substring):
                result += k
                break
    # log(result)
    return result


def solve_test_case(arr, qrr):
    res = []
    for query in qrr:
        l, r = query
        substring = arr[l-1:r]
        val = f(substring)
        log(val)
        res.append(val)
    return res


def generate_string(length):
    import string
    return ''.join(random.choice("abcde") for _ in range(length))

def generate_test_cases(num_cases, max_n, max_q):
    test_cases = []
    for _ in range(num_cases):
        n = random.randint(2, max_n)
        q = random.randint(1, max_q)
        s = generate_string(n)
        queries = []
        for _ in range(q):
            l = random.randint(1, n-1)
            r = random.randint(l+1, n)
            queries.append((l, r))
        test_cases.append((n, q, s, queries))
    return test_cases

# Generate random test cases
num_cases = 50000
max_n = 10
max_q = 1
test_cases = generate_test_cases(num_cases, max_n, max_q)

# Print the test cases
# print(num_cases)
for test_case in test_cases:
    n, q, s, queries = test_case
    # assert solve_test_case(s, queries) == solve(s, queries), (solve_test_case(s, queries), solve(s, queries), s, queries)


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    n,q = list(map(int,input().split()))
    srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(q)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr, mrr)  # include input here
    # assert solve_test_case(srr, mrr) == solve(srr, mrr), (solve_test_case(srr, mrr), solve(srr, mrr), srr, mrr)

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
