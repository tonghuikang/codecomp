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

class ManhattanDistanceFinderWithPoint:
    def __init__(self, points: List[Tuple[int, int]]):
        # Initial values for max and min distances and corresponding points
        self.max_x_plus_y = (float('-inf'), None)
        self.min_x_plus_y = (float('inf'), None)
        self.max_x_minus_y = (float('-inf'), None)
        self.min_x_minus_y = (float('inf'), None)
        self.max_minus_x_plus_y = (float('-inf'), None)
        self.min_minus_x_plus_y = (float('inf'), None)
        self.max_minus_x_minus_y = (float('-inf'), None)
        self.min_minus_x_minus_y = (float('inf'), None)

        for point in points:
            x, y = point
            self.max_x_plus_y = max(self.max_x_plus_y, (x + y, point))
            self.min_x_plus_y = min(self.min_x_plus_y, (x + y, point))
            self.max_x_minus_y = max(self.max_x_minus_y, (x - y, point))
            self.min_x_minus_y = min(self.min_x_minus_y, (x - y, point))
            self.max_minus_x_plus_y = max(self.max_minus_x_plus_y, (-x + y, point))
            self.min_minus_x_plus_y = min(self.min_minus_x_plus_y, (-x + y, point))
            self.max_minus_x_minus_y = max(self.max_minus_x_minus_y, (-x - y, point))
            self.min_minus_x_minus_y = min(self.min_minus_x_minus_y, (-x - y, point))

    def furthest_point_and_distance(self, x: int, y: int) -> Tuple[Tuple[int, int], int]:
        # Calculate distances and corresponding points
        potential_distances = [
            (abs(x + y - self.max_x_plus_y[0]), self.max_x_plus_y[1]), 
            (abs(x + y - self.min_x_plus_y[0]), self.min_x_plus_y[1]),
            (abs(x - y - self.max_x_minus_y[0]), self.max_x_minus_y[1]), 
            (abs(x - y - self.min_x_minus_y[0]), self.min_x_minus_y[1]),
            (abs(-x + y - self.max_minus_x_plus_y[0]), self.max_minus_x_plus_y[1]), 
            (abs(-x + y - self.min_minus_x_plus_y[0]), self.min_minus_x_plus_y[1]),
            (abs(-x - y - self.max_minus_x_minus_y[0]), self.max_minus_x_minus_y[1]), 
            (abs(-x - y - self.min_minus_x_minus_y[0]), self.min_minus_x_minus_y[1])
        ]

        # Find the furthest distance and corresponding point
        furthest_distance, furthest_point = max(potential_distances, key=lambda x: x[0])
        return furthest_point, furthest_distance

# # Example usage
# finder_with_point = ManhattanDistanceFinderWithPoint(points)

# # Query for a specific point
# furthest_point, furthest_distance = finder_with_point.furthest_point_and_distance(*query_point)
# furthest_point, furthest_distance


# # Example usage
# points_example = [(1, 3), (4, 2), (5, 5), (3, 3), (0, 0), (6, 6)]
# queries_example = [(1, 1), (4, 5), (3, 4)]

# # Get the furthest points for each query
# furthest_points_queries(points_example, queries_example)


def solve_(n, arr, brr):

    a2 = []
    b2 = []

    for a,b in zip(arr, brr):
        if a > b:
            a,b = b,a
        a2.append(a)
        b2.append(b)

    arr = a2
    brr = b2

    reference_sum = sum(abs(a-b) for a,b in zip(arr, brr))
    maxres = reference_sum

    return maxres + 2 * max(0, max(arr) - min(brr))


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
