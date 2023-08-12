#!/usr/bin/env python3
import sys
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

# import itertools

# for n in range(1,300):
#     arr = list(range(1,n+1))
#     maxval = 0
#     maxcomb = tuple(arr)
# #     for comb in itertools.permutations(arr):
# #         val = sum(i*x for i,x in enumerate(comb, start=1)) - max(i*x for i,x in enumerate(comb, start=1))
# #         if val >= maxval:
# #             maxcomb = comb
# #         maxval = max(maxval, val)
# #     print(maxval, end=", ")
# #     print(maxval, maxcomb)

#     for i in range(n):
#         comb = arr[:i] + arr[i:][::-1]
#         val = sum(i*x for i,x in enumerate(comb, start=1)) - max(i*x for i,x in enumerate(comb, start=1))
#         if val >= maxval:
#             maxcomb = comb
#         maxval = max(maxval, val)
#     print(maxval, end=", ")
# #     print(maxval, maxcomb)

    
        

arr = [
    0, 2, 7, 17, 35, 62, 100, 152, 219, 303, 406, 530, 678, 851, 1051, 1280, 1540, 1834, 2163, 2529, 2934, 3380, 3869, 4403, 4985, 5616, 6298, 7033, 7823, 8670, 9576, 10544, 11575, 12671, 13834, 15066, 16369, 17745, 19196, 20724, 22332, 24021, 25793, 27650, 29594, 31627, 33751, 35968, 38280, 40690, 43199, 45809, 48522, 51340, 54265, 57299, 60444, 63702, 67075, 70565, 74175, 77906, 81760, 85739, 89845, 94080, 98446, 102945, 107579, 112350, 117260, 122312, 127507, 132847, 138334, 143970, 149757, 155697, 161792, 168044, 174455, 181027, 187762, 194662, 201730, 208967, 216375, 223956, 231712, 239645, 247757, 256050, 264526, 273187, 282035, 291072, 300300, 309722, 319339, 329153, 339166, 349380, 359797, 370419, 381248, 392286, 403535, 414997, 426674, 438568, 450681, 463015, 475573, 488356, 501366, 514605, 528075, 541778, 555716, 569891, 584305, 598960, 613858, 629001, 644391, 660030, 675920, 692064, 708463, 725119, 742034, 759210, 776649, 794353, 812324, 830564, 849075, 867859, 886918, 906254, 925869, 945765, 965944, 986408, 1007160, 1028201, 1049533, 1071158, 1093078, 1115295, 1137811, 1160628, 1183748, 1207173, 1230905, 1254946, 1279298, 1303963, 1328943, 1354240, 1379856, 1405794, 1432055, 1458641, 1485554, 1512796, 1540369, 1568275, 1596516, 1625094, 1654011, 1683269, 1712870, 1742816, 1773109, 1803751, 1834744, 1866090, 1897791, 1929849, 1962267, 1995046, 2028188, 2061695, 2095569, 2129812, 2164426, 2199413, 2234775, 2270514, 2306632, 2343131, 2380013, 2417280, 2454934, 2492977, 2531411, 2570238, 2609460, 2649080, 2689099, 2729519, 2770342, 2811570, 2853205, 2895249, 2937704, 2980572, 3023855, 3067555, 3111674, 3156214, 3201177, 3246565, 3292380, 3338624, 3385299, 3432407, 3479950, 3527930, 3576350, 3625211, 3674515, 3724264, 3774460, 3825105, 3876201, 3927750, 3979754, 4032215, 4085135, 4138516, 4192360, 4246669, 4301445, 4356690, 4412406, 4468595, 4525259, 4582400, 4640020, 4698122, 4756707, 4815777, 4875334, 4935380, 4995917, 5056947, 5118472, 5180494, 5243015, 5306037, 5369562, 5433592, 5498129, 5563175, 5628732, 5694802, 5761387, 5828489, 5896110, 5964252, 6032917, 6102107, 6171825, 6242072, 6312850, 6384161, 6456007, 6528390, 6601312, 6674775, 6748781, 6823332, 6898430, 6974077, 7050275, 7127026, 7204332, 7282195, 7360617, 7439600, 7519146, 7599257, 7679935, 7761182, 7843000, 7925392, 8008359, 8091903, 8176026, 8260730, 8346017, 8431889, 8518348, 8605396, 8693035, 8781267, 8870094, 
]

def solve_(n):
    # your solution here

    return arr[n-1]


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
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
