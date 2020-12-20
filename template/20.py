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


from ortools.sat.python import cp_model

def solve_(inp):
    
    model = cp_model.CpModel()

    square_length = int(math.sqrt(len(inp)))
    num_edges = square_length*square_length*4
    num_spaces = num_edges
    # (square_length*square_length*4 - square_length*4)// 2

    indexes = [k for k,v in inp]
    edges = [0 for _ in range(num_edges)]
    assgn = [0 for _ in range(num_edges)]

    for i in range(4):
        edges[i::4] = [v[i] for k,v in inp]
        assgn[i::4] = range(square_length*square_length)

    log(edges)
    log(assgn)
    # i.e. assign edges to spaces
    # adj spaces has to be equal
    # spaces in the same square has to be equal

    # binary variables - whether are we assigning edge (144*4) to space (144*4 - 12*4)
    var = [[model.NewBoolVar('') for _ in range(num_edges)] for _ in range(num_spaces)]

    # for every space, you have to assign one edge
    for i in range(num_edges):
        model.Add(sum(var[i]) == 1)

    # for every edge, you have to assign to one space
    for i in range(num_spaces):
        model.Add(sum([row[i] for row in var]) == 1)

    # adjacent spaces should have and equal edge
    # left = right
    for i in range(square_length):
        for j in range(square_length-1):
            model.Add(sum(a*b for a,b in zip(var[(i*square_length+j)*4+0], edges)) == 
                      sum(a*b for a,b in zip(var[(i*square_length+j+1)*4+1], edges)))

    # up = down
    for i in range(square_length-1):
        for j in range(square_length):
            model.Add(sum(a*b for a,b in zip(var[(i*square_length+j)*4+2], edges)) == 
                      sum(a*b for a,b in zip(var[((i+1)*square_length+j)*4+3], edges)))

    # each edge in a square should belong to the same square
    for i in range(square_length):
        for j in range(square_length):
            model.Add(sum(a*b for a,b in zip(var[(i*square_length+j)*4+0], assgn)) == 
                      sum(a*b for a,b in zip(var[(i*square_length+j)*4+1], assgn)))

            model.Add(sum(a*b for a,b in zip(var[(i*square_length+j)*4+1], assgn)) == 
                      sum(a*b for a,b in zip(var[(i*square_length+j)*4+2], assgn)))

            model.Add(sum(a*b for a,b in zip(var[(i*square_length+j)*4+2], assgn)) == 
                      sum(a*b for a,b in zip(var[(i*square_length+j)*4+3], assgn)))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 10.0
    status = solver.Solve(model)
    
    log(status)
    log(cp_model.UNKNOWN, cp_model.FEASIBLE, cp_model.INFEASIBLE, cp_model.OPTIMAL)
    if status == cp_model.OPTIMAL:
        print("ok")

    return 0


def solve(inp):
    # screen input
    inp = sorted((k,v) for k,v in inp.items())

    if OFFLINE_TEST:
        log("----- solving ------")
        log(inp)
        log("----- ------- ------")
    
    return solve_(inp)


def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def parse_int(tupley):
    return int("".join(tupley),2)

def process(string_input):
    string_input = string_input.strip()

    # d = {}
    edges = {}

    for block in string_input.split("\n\n"):
        block = block.split("\n")
        log(block)

        idx = block[0][-5:-1]
        blk = [["1" if cell == "#" else "0" for cell in row] for row in block[1:]]
        # d[int(idx)] = blk
        edges[int(idx)] = (parse_int(blk[0]), parse_int(blk[-1]), 
                           parse_int([row[0] for row in blk]), 
                           parse_int([row[-1] for row in blk]))

    return edges


sample_input="""
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
"""

sample_input = sample_input.strip()
sample_input = process(sample_input)

sample_res = solve(sample_input)
print(sample_res)


test_input="""
Tile 2729:
.....#####
##..##.#.#
......#.##
#....#.#.#
#......##.
#...#..#.#
#.........
.......##.
#.#..#....
#.#.###..#

Tile 3673:
##.....###
.....##...
#.......#.
..#..##.##
...##.#...
...#......
..#...#..#
..........
##..#.#..#
####.#.#.#

Tile 2797:
#######..#
###..#.#.#
#...#.....
....#...#.
....#...#.
#...##....
....#....#
#..#......
.#........
#.#.....##

Tile 3779:
....###..#
#..#......
...##.....
#.#..#...#
..##.#....
##.##....#
#.........
.....#...#
#.###...#.
.#####.#.#

Tile 3217:
...###.###
#....#..##
#.......#.
......#..#
#...##..##
##..#....#
#...####.#
..#..##...
..#.##...#
#..#.###..

Tile 3137:
.#..#.#.#.
#.......#.
###...#..#
#.#...#...
.....#.#.#
..#..#....
#...#.#.##
..#......#
..#...#...
###.##.##.

Tile 2857:
...##..##.
.........#
#........#
.#.....#..
#..#..#...
#...#.#.#.
##....####
#.....##.#
...#..#...
..####....

Tile 1831:
#.##..####
.#.#.#...#
#..##.....
#..#....#.
#.##......
...#....#.
......#..#
..........
####..#...
####.###..

Tile 2423:
...#.##..#
#...##...#
##......##
...#.#....
#.....#...
#.....#..#
.#..####..
.##...#.##
..##.#..#.
#..#..####

Tile 3221:
..#.##.###
#.#.......
#...#....#
...#...#..
#..#.#...#
....###..#
.........#
.........#
#...#.##.#
##..##.###

Tile 2707:
.##.#.#...
.#.##..#.#
#...#.....
#.#.......
#...#.....
..#......#
.......###
..#.#...#.
#.#.......
..#...#.##

Tile 3041:
#.####...#
##.....#..
..#.#..###
#.###..###
.#.#.....#
#....#....
..##......
.###....#.
###.##.#..
#####.##.#

Tile 1627:
.###..#..#
.#..#.##..
##...#...#
#....###.#
..#......#
#....#..#.
#.##.....#
.##..#...#
..#...#..#
...#.###.#

Tile 1237:
...##..###
#.#......#
#.##..#..#
#.#.....#.
#....#...#
...#....#.
#.#....#..
.##.......
..#..#..##
.###.#.#.#

Tile 1187:
#...###...
#.###.#...
..##...#..
##.....#..
.....#...#
#.....#...
....#..#.#
.........#
.#...#....
.####.#.##

Tile 1361:
.#.##..###
......#..#
....#.#..#
.#.......#
#.#.....##
.#.#..##..
##.##....#
#.##..#.##
#.#......#
.##..##...

Tile 2087:
###.#.....
.#...#....
.#..#.....
####.....#
...#.....#
...##.....
##..###..#
....##..#.
.#.####...
...#..####

Tile 1129:
###.#.#...
#.##..###.
.....#....
#...#..#..
#.#.###.#.
.##..###..
#...##..##
.....#...#
#........#
...#..####

Tile 1093:
.....##.##
#.......##
.##.#.##.#
#.#..####.
#....#....
###......#
#.#.......
#..#.....#
#..#.#.#..
#..#....#.

Tile 3049:
##...#..##
#........#
#......#..
.....#.###
#........#
#..#.#....
#........#
....#.....
..##.....#
##.#..##.#

Tile 2399:
##...#.##.
...#......
#.#.##...#
##.......#
#.........
#.........
.....##..#
#....#....
.........#
.....##.##

Tile 3371:
##....##..
.....##...
##.##.#.##
......###.
##..####.#
..#..##..#
.....#...#
#..#..#..#
.##.#...##
.####..###

Tile 3343:
#......##.
.##.#.#..#
#...#.##.#
.##..##...
.#.#....##
##.#..#...
#....#.#.#
.....##..#
#.....##.#
.##.#....#

Tile 2393:
.####.#.#.
.#..##....
.##..#.#..
#....#....
#...##.##.
.#...#...#
#..#......
....#.##.#
#....##..#
.#..###.#.

Tile 1621:
##..###..#
##.....#..
#.#....###
.##..#.#.#
#.........
#......#.#
#.#.......
.#........
#.#......#
....####.#

Tile 3181:
#...#.####
...#.#...#
..........
....#..#..
##........
......####
#.#..#..##
..........
..#....##.
...###...#

Tile 2441:
.#..#..#..
#....##...
.#...#.#..
#...##..#.
...#..###.
.....#.#.#
#...#...#.
#...##...#
#......#.#
#...##..##

Tile 2389:
.#...#.#..
.........#
..........
###.......
....#.#...
....#.##..
#.....##.#
..#.......
#.##.....#
#...###.##

Tile 1847:
#.###.#..#
#.#...#.#.
#.......##
#...#..#.#
..###.#..#
...##....#
#....#...#
##...#...#
.###...#..
.#.#.####.

Tile 1871:
.###.##...
#.......#.
#.......#.
#.....#..#
..##...#.#
##.....###
.....###..
#....###.#
##.##..#..
###...####

Tile 3877:
#.....#.#.
..##....##
###......#
#...###...
.##...##..
.#...#....
..#....#.#
#.........
...#..#...
#..###.#..

Tile 3517:
###..##.#.
...###...#
..#......#
.#.#...#.#
....#.##.#
#...#..#..
...##....#
#.....###.
.#..##...#
........##

Tile 2609:
#...#..###
.........#
...#.#.#..
#####..#.#
#.#....#.#
.......#..
###..#...#
..........
.#...#....
#.#.....#.

Tile 3001:
..#...#...
#........#
#..#.....#
.#.#.#...#
#..##.....
#.....##..
#......#.#
..##...#..
.#..#.##.#
#.##.#####

Tile 3067:
#.#.#.###.
##....#...
.#..#.....
....#.....
.###..#.##
.....#....
.#...##...
.#.#.##..#
.....#...#
#.#.#....#

Tile 1583:
####....#.
##.#....##
##..#....#
#...#.##..
....##....
###.##...#
#..#..##.#
.###.....#
.#.##....#
..#.####.#

Tile 1741:
#.#.#####.
....#.....
#.#......#
..##...###
......#...
#........#
..##...###
#.#...####
####.#....
.#..#.#.#.

Tile 1933:
#####..###
#...#..#..
.##...#..#
.......###
##........
..#...##..
.....#..##
#....#....
#.....#.#.
....##..#.

Tile 3697:
#..#.#####
...#..##..
#.....#...
.#..#.##..
......#...
#......#..
##....#..#
.##.....#.
#.#..#....
#..##...##

Tile 1429:
##.....#..
###.#...##
#.....#..#
#...###..#
....#.....
##.#...#..
#....##...
.##.#..#..
..#.#.#..#
#.#.###...

Tile 1721:
##..#.#..#
...#.#....
##...#.#.#
##..#....#
.##.#....#
#..#.#....
#.##.#....
##.....#..
..#..###..
..###.#..#

Tile 1867:
.##.####.#
#.##....#.
#....#....
##..#..#..
##.#..#..#
.......#..
##........
..#...##.#
....#..#.#
..###.#.##

Tile 2143:
##..##.#..
#.........
..#.#..###
.#.#..#...
.#######..
....#....#
##.##.#..#
......##..
..#.#.##.#
..#...#..#

Tile 1657:
......#..#
#.##..###.
.#.....#.#
.#......##
#.####...#
...#.#....
#.#....###
#.....##.#
....#....#
#..#..#...

Tile 2719:
#####..#..
#.....###.
.##....###
..#.##....
#..##.....
.......###
#.....#...
..#...##..
.#..##.#.#
..####....

Tile 2803:
###..###..
.#..#...##
#.....#...
#.#.###...
##..#....#
#...#..#.#
...##...##
......####
.......##.
.###.#..##

Tile 3929:
.#.#####.#
##...#....
...#.#.#.#
.#......#.
.......#..
##....##.#
...#...#..
.......###
.........#
..##..##.#

Tile 1321:
.#.#...#.#
.......#..
...#.####.
#.........
..#.#.#.##
##....#...
..........
#.##...#..
#....#...#
#######.##

Tile 1153:
.#...#.###
#........#
#...#...#.
#.....#..#
#........#
#.#.....##
.....##...
#..#...#..
#.....#..#
##.#..##.#

Tile 3803:
#.####...#
#.##..#...
##..#.....
.##.....#.
..#...#...
#.##.#.#..
##.....#.#
##.#..#..#
##..#..#..
....##..##

Tile 2791:
.#....####
#.....#...
#.#.##...#
..#.#.#..#
##..#....#
#....#..##
...#.##..#
......#..#
#....#.#..
#.###.#.#.

Tile 3529:
.#...#...#
.....#..#.
#........#
.........#
.##.##.#..
##.......#
#...#...##
.......#..
...#.##..#
#.#####...

Tile 3257:
####.#.###
.##...##..
..#....#..
..###..#.#
#.#..#...#
.......##.
##.##.####
.....##..#
#....##...
###..###.#

Tile 1531:
#.#...#...
.........#
##...#...#
##......##
...#.....#
#.#.###..#
#....#...#
.#....#.#.
#...#....#
#########.

Tile 3413:
#...#.....
...###..##
##..##....
.#..##....
#..#.#.#..
...#.....#
....#..#.#
...#....##
...#.#...#
#.###..#.#

Tile 1117:
#.#.##...#
.........#
.........#
#....#..##
#.#.##..#.
#......#..
#.#.#.#...
#..#.....#
......#.#.
..##.#..#.

Tile 1499:
.#####..##
...#...###
.........#
#..#.....#
##......##
#.......#.
#......##.
#####.....
.#.....#..
.###..####

Tile 1787:
.######..#
#....#.#.#
........#.
#.....#...
..........
..#..#.###
#.#..#...#
.#.#.#####
.....#.#.#
##.#.##.##

Tile 1949:
##..####.#
##.#......
.........#
....#..#.#
.#...##..#
....#..#..
#.....#...
##....#..#
.....#..#.
.#.#.#.#.#

Tile 2161:
####.#..#.
#.......#.
.##....#.#
.###..#..#
#.#..#....
#..#..#...
#...#.#.##
#...#.##.#
###....#..
#...#.##.#

Tile 2953:
#.#...#.##
#.#.#...##
#.......##
.........#
#..#.....#
..#.##.#..
..#.###..#
##.....#..
......#...
###.#.#.#.

Tile 1039:
##..###..#
#.....#...
#....#.#.#
#...#...##
##.......#
#.....#..#
...#.....#
.#.###...#
.........#
#.#..#####

Tile 2027:
##.####..#
..#.....#.
#.#.##...#
.#.......#
.....#.###
#........#
.#.#.....#
#.#...#.#.
#.###...#.
..##.##...

Tile 1889:
..####.##.
#....#.#.#
##.#..##.#
#..#...###
##...#..##
#..##...#.
#..#.###.#
#.###.#...
##...##...
##.##..###

Tile 3557:
##.##.#...
.....#.#.#
#.#..#....
##..###..#
....##...#
....#....#
.#..#...#.
.#.#.##..#
###..#...#
#.#.#..#..

Tile 2549:
....#..#..
#..#..#.##
.....#...#
#..##.#.#.
.#.##....#
.#..#....#
.#.#...#..
##.....#..
..........
#....#...#

Tile 1543:
.##.###.##
....#.#..#
#.........
...#.#...#
#.......#.
.....##...
....#.....
..###.#..#
###..#....
###.#.###.

Tile 2417:
.#....#.#.
#.#..###.#
....##....
##.....#.#
..........
#....#..##
.....#...#
#.#......#
#........#
###..##..#

Tile 3541:
.##..###..
##...##.##
##..#....#
.........#
...#.#....
...#.....#
#..#...#..
..........
.#..##.#.#
..##.#..##

Tile 1931:
.##...##.#
...#.....#
#...###...
#.......#.
#.......##
.#.#.#....
##..#....#
##...#..##
..........
....#.#.#.

Tile 2833:
.#...#....
#..####...
.#...##.##
.#.......#
#.#...#..#
..#.....##
#......#..
##....#..#
......#..#
##..##...#

Tile 3301:
###.#.####
..###.##..
..........
.#....##..
#.#..##...
..#....#.#
.#.#..#...
#.#..#...#
....#.##.#
......##.#

Tile 3671:
##.#..#...
.##....###
##.....#..
###.#.#.#.
....#...##
#.....#..#
#.#......#
.......###
#..#.....#
...#.###.#

Tile 1609:
..##..#.##
###..##...
.#..#..#..
#....#.#..
#..#.##.#.
#.......#.
.....#...#
#.....#..#
......##..
###..##...

Tile 2957:
###..#####
###.......
#..#.....#
#.#......#
#.....#..#
#.#.......
###.#..#.#
.#.#.##.#.
###.#.#...
...##.####

Tile 2467:
##.#.#.#..
........#.
....#...#.
#.......#.
..#...#..#
...#.#...#
#...###.##
#.##.#.#..
.#...##...
..#.####..

Tile 1907:
###..###.#
#...#....#
...#..#..#
.......#.#
........##
##...#..##
#..#.##...
#....#.#.#
#......###
###.....#.

Tile 2251:
##...#..##
#..#.##..#
..#.#..###
##........
.......#..
.#..#.#...
#..#.#..#.
#..#......
###.#...##
#.###.##..

Tile 2657:
.#..##..##
##.#....##
#.#...#...
#..#......
#........#
#.........
..#....#..
#.........
#.........
##.###.###

Tile 2671:
#.#.#.##.#
.#..#..#.#
.#.......#
#...#..#..
.....###.#
#.....#..#
#.#......#
#........#
#....#....
####.#..#.

Tile 3121:
..#..#...#
#....#...#
....###.#.
#........#
..####....
.......###
#..#.####.
##.#.###.#
.####..#..
#.#...#..#

Tile 1021:
#####.####
#....#...#
####....#.
#......#..
##..#...##
##.#.#..##
#.....#.#.
#.#...##.#
.#......##
.#.##...#.

Tile 1019:
...#.##..#
#........#
.........#
##....#...
#..#..##.#
........#.
.....##...
#..##....#
#.....#.#.
.##.####..

Tile 2099:
#.##..###.
#..#......
#.##...#.#
...##..##.
#...#.....
.#.....#.#
.....#..#.
.....##...
#...##..##
##.#####.#

Tile 1297:
.###..####
##...###.#
..#..##..#
#...#.....
...#....##
#....#...#
###.##.#..
#.........
......#.##
..#.##..#.

Tile 1993:
####..#.#.
.#.#.#....
#...#.##.#
#.....#..#
..#..#.#..
#.#.#...#.
.#..#...#.
##...##..#
..#...##.#
#..#.##.#.

Tile 2617:
..#.#.#.##
.##.####..
#.#..####.
....#.#..#
#.#.#.#.##
...#......
##......##
.#...#.#..
#..#...#.#
.###.#..#.

Tile 1009:
##.#....#.
#.#.#...#.
#.#....#..
......#..#
####......
....#...##
......#..#
.......#..
##.....#..
..#...#.#.

Tile 2203:
#.#.###.##
#.#...##.#
....#.##.#
#..#......
.#....#..#
......#...
##.##....#
#...#...#.
##.##....#
#..#..#.##

Tile 3467:
....##.##.
#...#..#..
##....#...
#.......##
#.........
...#....##
#...#.....
##.#.#.#.#
...##.#..#
#...#.....

Tile 3617:
##..####.#
#...#.#..#
.......#.#
..........
.......#..
...#...###
#.#.......
#.........
.....##...
##.#.###..

Tile 1601:
.#..####.#
.....##...
#.....##.#
#...###..#
##....#...
##......#.
#.#.....#.
##.......#
#.......##
..##.#.#..

Tile 2699:
.#...#...#
#.##...##.
..........
#.##..#.#.
...#..#..#
...#.##..#
#.#..#..##
.#...###..
.#.......#
##..###.##

Tile 1231:
#.....##..
#..#.....#
###..#.#.#
..######..
...##....#
#..#...#.#
.....#...#
#.##..####
..#.#.....
.###.##..#

Tile 3373:
###...#...
.##..#...#
.#.#.....#
........#.
....#.....
#....#....
##.....#.#
###.......
#......#.#
#.#..#####

Tile 1901:
##.##..##.
##...#..##
......#..#
.#.#......
#.###.#..#
##.#.#.#..
........##
#....#..#.
.....#...#
.#..##....

Tile 1213:
...#.#.#.#
#.##...#..
.#.##.####
.....####.
##.##....#
#..#...#..
....#.....
##........
##..##....
###...#...

Tile 3163:
#.....#.#.
###.#..#..
......#...
#..#.#....
##....#.#.
##.#..##..
#.##.#..##
.#........
.#...#....
.....#.##.

Tile 2053:
.###.#...#
#.....#...
#..#.#..##
##.......#
#..#....##
....###..#
#.#..#...#
#.##.#.#..
.#..#..#.#
#.......##

Tile 3229:
......#...
#...#....#
##....#..#
.#..#.##.#
..####.#.#
###.......
##....#...
#..#...#.#
........#.
.#.###.###

Tile 3271:
#....#.###
#.......#.
#......#..
.###..##.#
....#..#..
.....#..##
.#...#....
........##
.......##.
#..####.##

Tile 2003:
..#.#....#
.##..#...#
#.........
#.........
#.........
#.##...#..
#..#..##.#
.......#..
##.......#
..#####..#

Tile 3637:
##.##.####
....#.#..#
##.#...#.#
....###.##
..........
.##.###.#.
#.###.....
......#...
..##.....#
##.#######

Tile 3967:
#..#.####.
###..#....
#.........
#..#..#..#
#..#.....#
..#...#...
..###.#.#.
#..#.....#
.#......#.
...##.#..#

Tile 2621:
...##.###.
...#.....#
#.#.##....
#.#.......
##.#.#.#..
...#....##
.......###
..##....##
#.#..#....
#####...#.

Tile 3347:
####..##..
#.#.##....
...#.##...
....##.#.#
####...###
..##..#..#
......#..#
#....#.#..
#....##..#
.#.#.#...#

Tile 1319:
#..###...#
#..##.#..#
#........#
##...#.#.#
#.##....#.
.....#.#.#
#...#....#
.....#...#
#.........
.#.##.....

Tile 1279:
##.....###
##...#....
#....#..##
#...##...#
...#.###.#
.#........
#.....##.#
...#.....#
..###.....
#.#.#..##.

Tile 1861:
.##...#.#.
#....####.
..........
#.#...#..#
###.####..
#......#.#
.......#.#
#.#.#.#..#
##.....#.#
....##..##

Tile 2861:
.#.######.
..#.#..##.
#.##......
....#.#...
........##
#....##...
......#...
#.#.......
#.#....#..
#######..#

Tile 1879:
#..#.....#
#........#
#..#####..
#.#..#..#.
#........#
.#....##.#
.##.....##
...#.....#
.##......#
..###.##.#

Tile 1291:
......##..
.#.....###
...#.#....
#....#.#.#
###.......
....#.....
.#.#.#.#..
.#.##....#
#..#.#....
##..##..#.

Tile 1109:
#....##.##
#.##....##
..#......#
.........#
..#.##.#..
#........#
##.#.....#
##....#...
.......###
##...#.#.#

Tile 2333:
......#..#
##..####..
..#.......
#.........
#.#.##...#
#.........
#.......#.
#.##.#..##
.#..#..#..
###..##..#

Tile 2081:
####...#.#
.....#....
.....##..#
.#..#..#.#
#.........
..##.#...#
.......###
.#..#.....
#......##.
#.#.#.#.##

Tile 1489:
#..##.#..#
..#.#.#.#.
...#......
#........#
#.#.#.....
.#.#.#.#.#
#.##......
#.#.##.#.#
#.#......#
.#..#..#.#

Tile 3931:
##.###.#.#
#........#
#.....#..#
.###......
......##.#
#..#...###
..#......#
#..#......
#....##...
###.###.##

Tile 1249:
.###.###.#
#.##...###
...#.#....
#...#..#..
......#..#
#......###
##..#...#.
..##.....#
#..#.#....
##....####

Tile 2381:
#...#....#
.#...##..#
##...##..#
...#.#...#
#..##.#...
.##..#.##.
.....####.
#..#..##.#
##...##...
.##.######

Tile 1747:
.####..#.#
#........#
....#....#
#.....####
##..#.#..#
###.##..##
.##...#...
..##......
#....###..
.#####..##

Tile 2687:
#.#.....#.
.........#
#..#...#.#
..........
#......##.
..#...##..
##.##...##
##.#...##.
......#..#
.#.#....#.

Tile 1327:
.###.#####
.......#.#
#..#..#.#.
#...#..#..
.......#..
..#.#.....
#........#
.##....#..
..###.#..#
#..#.##.##

Tile 3727:
#.#..#...#
..#.#....#
.##.###.#.
#.........
##.#...#.#
##.#....##
.##...#...
......#..#
........#.
#....##.##

Tile 2341:
.##.#.####
...#....#.
.#.....#.#
.....#....
#.#.###.#.
##.##.....
#...#.....
..#.#..#..
........#.
#.##......

Tile 1439:
#..#.#..##
.......#..
....#..##.
..#..#.#..
.....#...#
.#..#.##..
#...#..#.#
#.#......#
.#..#.....
##.#...#.#

Tile 2351:
..###...##
#....###..
.#....#..#
.#...#....
.#.......#
..#....##.
#..#.....#
#.......#.
##..#..#.#
...#..##..

Tile 2269:
.#####...#
#........#
#.......##
#.#....#..
..##.....#
.#..#..#.#
##...##...
#......###
...#......
#.#.###.#.

Tile 2887:
.#.##.#.##
.#....#...
#.....#..#
#.##...#.#
#...#.#.##
##.##.#...
##.#.##..#
.#.##..#..
......#..#
.#.#.##...

Tile 3391:
.####....#
.#..#..###
....#...#.
...#..#.##
#....#..##
#...#..##.
#..####.#.
..####..##
..##.....#
...#.#..##

Tile 3533:
.#....#..#
#.........
..#..#..##
.#.##.#..#
#...#.....
......##..
...#.#.#.#
#.....##..
..........
##.##..#..

Tile 1637:
.#.#.#.##.
#.#.....##
.#....#...
##.......#
.##.###.##
##.#......
..#.....#.
.###...#.#
........#.
#.##...#.#

Tile 3323:
..#.#.#.#.
#.#.....#.
#.##..#.##
##.......#
#.#....#.#
.##......#
.#..#..#..
..#..##..#
...##.....
##.##.##.#

Tile 1559:
##.##.#..#
.....#.#..
#.#.####..
...#.#...#
##....#..#
#.##...#..
.#..##.###
....#..#..
.#.#.#.#.#
#....#..#.

Tile 2039:
..#.######
.#...#...#
###.#.....
##..###..#
.#...##...
..#..#...#
#.....#.#.
....#.....
.###.....#
..##.#.###

Tile 3677:
####......
.......#..
#.........
........#.
.....###.#
#...#.###.
##........
....##..##
.#....#...
.##..##.#.

Tile 1973:
#.###..##.
#.........
#......###
#.#...####
#.#..#.#.#
..#..#..#.
#..#.#.#.#
##.##..#..
#.###...##
##.#.##.#.

Tile 2309:
####..##.#
#..#..#..#
...#.#...#
#....###.#
##....#.#.
....##....
......#...
##..#.....
#....#..#.
.##.#....#

Tile 2237:
.##......#
#.#....##.
...###..#.
#.#....###
.....#...#
#.##.....#
#..#...#..
.#...#..##
#.#....##.
....#.#.#.

Tile 2663:
##..##.###
#..#..##..
#...##...#
#.#.#..#.#
#..#......
....#..#.#
...#...###
##........
##....#.#.
.#...##.#.

Tile 1571:
##.#.#...#
.##.##.###
........##
#.........
#.#...##..
#.......#.
##..#####.
#..#...##.
##......#.
..#..##..#

Tile 3011:
#.#.#...##
....##.#.#
#...##...#
#........#
.#....#...
......#...
#.#.#..#..
..#####...
#.###.....
.......#.#

Tile 3457:
##.##..#.#
###.##....
.#.#...#..
##.......#
.....#.##.
#.#.##.#.#
.###.#####
..#.......
.##.....##
....#.###.

Tile 1619:
#..#...#..
#.....#.#.
#..#..##..
.....#....
#.#...#...
.#..#....#
#....##.##
.....##.#.
......####
#.#.#.##..

Tile 1663:
..#..###.#
#...#.#..#
#...#.....
###..##...
..#.#.....
..........
#.#....##.
..#....###
#..#..#.#.
###.#.##..
"""

test_input = test_input.strip()

# test_input = process(test_input)
# test_res = solve(test_input)
# print(test_res)



print(len(test_input.split("\n\n")))