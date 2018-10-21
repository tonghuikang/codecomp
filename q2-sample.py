# usage:  (python3 a.py < a.in) > a.out
import time, sys, inspect

lineno = lambda: inspect.currentframe().f_back.f_back.f_lineno
print = lambda *a, **k: __builtins__.print(str(lineno())+':', *a, file=sys.stderr, **k)

#---------------------------------------------

'''
this reminds me of that algorithm for polygon rasterization called 'scan-line conversion'

'''

import collections
import heapq

def run(data):
    a, b, c, n, q = data

    x1, x2, a1, b1, c1, m1 = a
    y1, y2, a2, b2, c2, m2 = b
    z1, z2, a3, b3, c3, m3 = c

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
                return ret_score
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
                return ret_score
                break

            prev_score = score
            heapq.heappush(active, mm)

            # print(mm, 'entering!')

            i += 1


    return 0



#---------------------------------------------

def read_case():
    n, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    return (a, b, c, n, q)

for i in range(int(input())):
    outstr = 'Case #'+str(i+1)+': '+str(run(read_case()))
    print(outstr, ' @ t =', time.clock())
    __builtins__.print(outstr)
