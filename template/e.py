import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(colors,exact,permute):  # fix inputs here
    console("----- solving ------")
    console(colors, exact, permute)
    if exact == permute == len(colors):
        return colors

    colors_original = [x for x in colors]

    missing_color = list(set(range(1,len(colors)+2)) - set(colors))[0]
    num_missing_color = len(colors) - permute

    if len(set(colors)) == 1:
        if exact != permute:
            return None
        return [colors[0] for _ in range(exact)] + [missing_color for _ in range(len(colors) - exact)]

    arr = sorted(colors)

    p = exact
    q = permute

    c = Counter(arr)
    hist_original = [[k,v] for k,v in sorted(c.items(), reverse=True, key=lambda x:x[1])]
    hist = [[k,v] for k,v in sorted(c.items(), reverse=True, key=lambda x:x[1])]
    console(hist)

    while p:
        if hist[0][1] >= hist[1][1]:
            hist[0][1] -= 1
            p -= 1
            continue
        else:
            idx = 1
            while idx < len(hist) and hist[idx][1] > hist[0][1]:
                hist[idx][1] -= 1
                p -= 1
                if not p:
                    break
                idx += 1

    console("post_removal")
    console(hist)

    max_remaining = max(x[1] for x in hist)
    console("max_remaining")
    console(max_remaining-num_missing_color, len(colors)-exact-num_missing_color)
    if max_remaining-num_missing_color > (len(colors)-exact-num_missing_color)/2:
        return None

    to_fill = []
    for k,v in hist:
        to_fill.extend([k]*v)
    console("to_fill and val")
    console(to_fill)

    halfway = int(len(to_fill)/2)
    to_fill_val = [x for x in to_fill[halfway:]] + [x for x in to_fill[:halfway]]
    to_fill_val[:num_missing_color] = [missing_color]*num_missing_color
    console(to_fill_val)

    to_replace = collections.defaultdict(list)
    for a,b in zip(to_fill, to_fill_val):
        to_replace[a].append(b)

    for (k1,v1),(k2,v2) in zip(hist_original, hist):
        # assert k1 == k2
        for _ in range(v1-v2):
            to_replace[k1].append(k1)

    console(to_replace)

    res = []
    for color in colors_original:
        val = to_replace[color].pop()
        res.append(val)

    # validate
    actual_exact = 0
    for a,b in zip(colors_original, res):
        if a == b:
            actual_exact += 1
    actual_permute = len(colors_original) - sum([v for k,v in (Counter(colors_original) - Counter(res)).items()])

    console(Counter(colors_original) - Counter(res))
    console(colors_original)
    console(res)
    console(actual_exact, actual_permute)
    console(exact, permute)
    assert exact == actual_exact
    assert permute == actual_permute

    return res


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    _, a, b = list(map(int,input().split()))
    colors = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(colors,a,b)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    if res == None:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(x) for x in res))
