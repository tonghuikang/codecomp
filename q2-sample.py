# usage:  (python3 a.py < a.in) > a.out
import time, sys, inspect

lineno = lambda: inspect.currentframe().f_back.f_back.f_lineno
print = lambda *a, **k: __builtins__.print(str(lineno())+':', *a, file=sys.stderr, **k)

#---------------------------------------------


cases = []
t = int(input())  # read a line with a single integer
for case_num in range(1, t + 1):
    N, Q = [int(s) for s in input().split(" ")]
    X1, X2, A1, B1, C1, M1 = [int(s) for s in input().split(" ")]
    Y1, Y2, A2, B2, C2, M2 = [int(s) for s in input().split(" ")]
    Z1, Z2, A3, B3, C3, M3 = [int(s) for s in input().split(" ")]
    cases.append([case_num, N, Q, X1, X2, A1, B1, C1, M1, Y1, Y2, A2, B2, C2, M2, Z1, Z2, A3, B3, C3, M3])

#---------------------------------------------


'''
this reminds me of that algorithm for polygon rasterization called 'scan-line conversion'

'''

import collections
import heapq

def solve(case):
    case_num, n, q, x1, x2, a1, b1, c1, m1, y1, y2, a2, b2, c2, m2, z1, z2, a3, b3, c3, m3 = case

    x = [x1, x2]
    y = [y1, y2]
    z = [z1, z2]
    for i in range(2,n):
        x.append( (a1 * x[i-1] + b1 * x[i-2] + c1) % m1 )
        y.append( (a2 * y[i-1] + b2 * y[i-2] + c2) % m2 )
    for i in range(2,q):
        z.append( (a3 * z[i-1] + b3 * z[i-2] + c3) % m3 )

    k = z
    k[0] += 1

    minmax = list( sorted(((-(min(x[i], y[i]) + 1), -(max(x[i], y[i]) + 1)) for i in range(n)), key=lambda x: x[1]) )
    active = [minmax[0]]   # min-heap
    prev_score = -minmax[0][1]+1
    cur_rank = 0
    i = 1
    print(' *** START ! *** ', k[0])

    while True:
        active_head = active[0] if len(active) else (1,1)
        mm = minmax[i] if i < len(minmax) else (1,1)
        # print(active_head, mm)

        if mm == active_head == (1,1):
            break

        if -active_head[0] > -mm[1]:
            # CASE:  active edge leaving
            score = -active_head[0]
            cur_rank += (prev_score - score) * len(active)

            # print(cur_rank, score, prev_score, active)

            if cur_rank >= k[0]:
                ret_score = score + (cur_rank - k[0]) // len(active)
                print('SCORE = ', ret_score)
                return case_num, ret_score
                break

            prev_score = score
            heapq.heappop(active)

            # print(active_head, 'leaving!')

        else:
            # CASE:  passive edge becoming active edge
            score = -mm[1]+1
            cur_rank += (prev_score - score) * len(active)

            # print(cur_rank, score, prev_score, active)

            if cur_rank >= k[0]:
                ret_score = score + (cur_rank - k[0]) // len(active)
                print('SCORE = ', ret_score)
                return case_num, ret_score
                break

            prev_score = score
            heapq.heappush(active, mm)

            # print(mm, 'entering!')

            i += 1


    return case_num, 0



#---------------------------------------------

import multiprocessing as mp
n_thread = mp.cpu_count()
with mp.Pool(n_thread) as p:
    results = p.map(solve, cases)

results.sort(key=lambda x: x[0])

for result in results:
    outstr = 'Case #'+str(result[0])+': '+str(result[1])
    print(outstr, ' @ t =', time.clock())
    __builtins__.print(outstr)