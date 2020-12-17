import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_(field):

    for _ in range(6):
        new_field = [[[0 for _ in range(dims)] 
                         for _ in range(dims)] 
                         for _ in range(dims)]
        for i,plate in enumerate(field[1:-1], start=1):
            for j,row in enumerate(plate[1:-1], start=1):
                for k,cell in enumerate(row[1:-1], start=1):
                    count = 0
                    for x in [-1,0,1]:
                        for y in [-1,0,1]:
                            for z in [-1,0,1]:
                                if x == y == z == 0:
                                    continue
                                if field[i+x][j+y][k+z] == 1:
                                    count += 1
                    if field[i][j][k] == 1:
                        if count < 2 or count > 3:
                            new_field[i][j][k] = 0
                    else:
                        if count == 3:
                            new_field[i][j][k] = 1
        totals = sum(sum(sum(row) for row in plate) for plate in new_field)
        log(totals)
        field = new_field
    
    return totals


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


dims = 20
mid = dims//2

def process(string_input):
    field = [[[0 for _ in range(dims)] for _ in range(dims)] for _ in range(dims)]

    for i,row in enumerate(string_input.split("\n")):
        for j,cell in enumerate(row):
            if cell == "#":
                field[mid][i+mid][j+mid] = 1
    return field

sample_input="""
.#.
..#
###
""".strip()


sample_input = sample_input.strip()
sample_input = process(sample_input)

sample_res = solve(sample_input)
# print(sample_res)


# test_input="""
# #.#.##.#
# #.####.#
# ...##...
# #####.##
# #....###
# ##..##..
# #..####.
# #...#.#.
# """.strip()

# test_input = test_input.strip()

# test_input = process(test_input)
# test_res = solve(test_input)
# # print(test_res)



