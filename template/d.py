#!/usr/bin/env python3
import sys
import math

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
# abc = "abcdefghijklmnopqrstuvwxyz"
# abc_map = {c:i for i,c in enumerate(abc)}
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


from typing import List, Tuple
# ---------------------------- template ends here ----------------------------

from typing import List, Tuple
import math

def furthest_point(points: List[Tuple[int, int]], queries: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    # Find extreme points
    max_x_point = max(points, key=lambda p: p[0])
    min_x_point = min(points, key=lambda p: p[0])
    max_y_point = max(points, key=lambda p: p[1])
    min_y_point = min(points, key=lambda p: p[1])

    def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    results = []
    for query in queries:
        # Calculate distances to the extreme points
        distances = [
            (euclidean_distance(query, max_x_point), max_x_point),
            (euclidean_distance(query, min_x_point), min_x_point),
            (euclidean_distance(query, max_y_point), max_y_point),
            (euclidean_distance(query, min_y_point), min_y_point)
        ]

        # Find the furthest point
        furthest_point = max(distances, key=lambda x: x[0])[1]
        results.append(furthest_point)

    return results

# # Example usage
# points_example = [(1, 3), (4, 2), (5, 5), (3, 3), (0, 0), (6, 6)]
# queries_example = [(1, 1), (4, 5), (3, 4)]

# # Get the furthest points for each query
# furthest_points_queries(points_example, queries_example)


def solve_(n, arr, brr):

    points = list(zip(arr, brr))
    queries = list(zip(brr, arr))
    # your solution here

    reference_sum = sum(abs(x-y) for x,y in zip(arr, brr))
    maxres = reference_sum

    # Find extreme points
    max_x_point = max(points, key=lambda p: p[0])
    min_x_point = min(points, key=lambda p: p[0])
    max_y_point = max(points, key=lambda p: p[1])
    min_y_point = min(points, key=lambda p: p[1])

    def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    results = []
    for query in queries:
        # Calculate distances to the extreme points
        distances = [
            (euclidean_distance(query, max_x_point), max_x_point),
            (euclidean_distance(query, min_x_point), min_x_point),
            (euclidean_distance(query, max_y_point), max_y_point),
            (euclidean_distance(query, min_y_point), min_y_point)
        ]

        # Find the furthest point
        a,b = max(distances, key=lambda x: x[0])[1]
        y,x = query
        res = reference_sum + abs(x-b) + abs(a-y) - abs(x-y) - abs(a-b)
        maxres = max(maxres, res)
        # results.append(furthest_point)

    return maxres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
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
    brr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, arr, brr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
