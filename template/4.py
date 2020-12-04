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


def solve_1_(strr):
    # your solution here
    lst = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for abc in lst:
        if abc not in strr:
            return 0
    return 1

def check_digit(strr):
    if strr[0] == "0":
        return False
    for s in strr:
        if s not in "0123456789":
            return False
    return True

def solve_2_(strr):
    # your solution here
    lst = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for abc in lst:
        if strr.count(abc) != 1:
            return 0
        
    d = {}
    for kv in strr.split():
        if kv.count(":") != 1:
            log("ERROR duplicate colon")
            return 0
        a,b = kv.split(":")
        d[a] = b
    

    if check_digit(d["byr"]) and 1920 <= int(d["byr"]) <= 2002:
        pass
    else:
        log("byr")
        return 0

    if check_digit(d["iyr"]) and 2010 <= int(d["iyr"]) <= 2020:
        log("")
        pass
    else:
        return 0

    if check_digit(d["eyr"]) and 2020 <= int(d["eyr"]) <= 2030:
        pass
    else:
        log("")
        return 0

    if d["hgt"].endswith("cm"):
        if not check_digit(d["hgt"][:-2]):
            log("")
            return 0
        if 150 <= int(d["hgt"][:-2]) <= 193:
            pass
        else:
            log("")
            return 0
    elif d["hgt"].endswith("in"):
        if 59 <= int(d["hgt"][:-2]) <= 76:
            pass
        else:
            log("")
            return 0
    else:
        log("")
        return 0            

    if d["hcl"][0] != "#":
        return 0

    if len(d["hcl"]) != 7:
        return 0
    
    for s in d["hcl"][1:]:
        if s not in "0123456789abcdef":
            return 0

    if d["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return 0

    if len(d["pid"]) != 9:
        return 0

    for s in d["pid"]:
        if s not in "0123456789":
            return False

    log("CHECK")
    log(strr)
    return 1


def solve_1(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_1_(*args)

def solve_2(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_2_(*args)


def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]


overall_res = 0
entry = []

# for case_num in range(323):
while True:
# for case_num in range(int(input())):

    # read line as a string
    strr = input().strip()
    if strr == "EXIT":
        sys.exit()
    entry.append(strr)
    if strr == "":
        overall_res += solve_2(" ".join(entry))
        entry = []

    print(overall_res)
