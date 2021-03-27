#!/usr/bin/env python3

import sys
import numpy as np
from scipy.stats import pearsonr
input = sys.stdin.readline  # to read input quickly


def solve(ref):
    # your solution here
    ref = [[int(x) for x in row.strip()] for row in ref]
    ref = np.array(ref)

    correct_for_each_question = np.sum(ref, axis=0)

    p_vals = []
    for result in ref:
        p_val = pearsonr(correct_for_each_question, result)[0]
        p_vals.append(p_val)
    cheater = np.argmin(p_vals)

    return cheater+1


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


num_cases = int(input())
input()
for case_num in range(num_cases):
    k = 100
    arr = read_strings(k)  # and return as a list of str
    res = solve(arr)  # include input here
    print("Case #{}: {}".format(case_num+1, res))
