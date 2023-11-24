#!/usr/bin/env python3
import sys

input = sys.stdin.readline  # to read input quickly

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




# ---------------------------- template ends here ----------------------------


def solve2_(n, arr):
    n = len(arr)
    # your solution here

    lrr = [x-i for i,x in enumerate(arr)]
    rrr = [x+i for i,x in enumerate(arr)]

    # log(lrr)
    # log(rrr)

    # go left then right

    lmax = [0, lrr[0]]
    for x in lrr[1:]:
        lmax.append(max(lmax[-1], x))

    rmax = [rrr[-1]]
    for x in rrr[::-1][1:]:
        rmax.append(max(rmax[-1], x))
    rmax = rmax[::-1]

    # log(lmax)
    # log(rmax)

    vals = []
    minval = 10**18
    for i,(l,r,x) in enumerate(zip(lmax, rmax, arr)):
        val = max(l+i, r, x)
        vals.append(val)
        minval = min(minval, val)

    # log(vals)

    return vals


def solve_wrong(n, arr):

    n = len(arr)
    # arr = minus_one(arr)

    w1 = max(i+x for i,x in enumerate(arr))
    w2 = max(i+x for i,x in enumerate(arr[::-1]))

    log(w1, w2)

    if len(arr) <= 2:
        return min(w1, w2)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    v1 = solve2_(n, arr)  # include input here
    v2 = solve2_(n, arr[::-1])  # include input here

    v1 = v1[1:-1]
    v2 = v2[::-1][1:-1]

    log(v1)
    log(v2)

    res = min(max(x,y) for x,y in zip(v1, v2))
    res = min(res, w1, w2)

    return res


def solve_(n, arr):
    lrr = [n-i-1+x for i,x in enumerate(arr)]
    rrr = [i+x for i,x in enumerate(arr)]

    log(lrr)
    log(rrr)

    log()

    lmax = [0] * n
    rmax = [0] * n

    lmax[0] = lrr[0]
    rmax[-1] = rrr[-1]

    for i in range(1,n):
        lmax[i] = max(lmax[i-1], lrr[i])
    
    for i in range(n-2,-1,-1):
        rmax[i] = max(rmax[i+1], rrr[i])

    minres = min(rmax[0], lmax[-1])

    for i in range(1,n-1):
        res = max(lmax[i-1], rmax[i+1], arr[i])
        minres = min(minres, res)

    log(lmax)
    log(rmax)

    return minres



for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):
    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    # print length if applicable
    # print(len(res))

    # res_wrong = solve_wrong(n, arr)
    res = solve(n, arr)

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
