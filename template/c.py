# to note - topcoder uses python 2.7
import heapq as hq
import math
from fractions import gcd  # instead of math.gcd

def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    weights = [float('inf')]*n   # instead of math.inf
    path = [None]*n
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                f = -gcd(g,w)
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return path, weights


class SquareCityWalking:
    def largestGCD(self, N, A):
        if N == 1:
            return A[0]
        G = [[] for _ in A]
        for x in range(N):
            for y in range(N):
                loc1 = x*N+y
                culture = A[loc1]
                for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                    x2, y2 = x + dx, y + dy
                    loc2 = x2*N+y2
                    
                    if not (0 <= x2 < N): 
                        continue
                    if not (0 <= y2 < N): 
                        continue
                   	
                    cost = gcd(A[loc1], A[loc2])
                    G[loc1].append((loc2, cost))
                    G[loc2].append((loc1, cost))
                    
        # print(G)
        res = dijkstra(G, 0)
        # print(res)
        return -res[1][-1]


s = SquareCityWalking()
print(s.largestGCD(5, [
 96, 48, 96, 96, 96,
 32, 11, 11, 11, 16,
 96, 11, 96, 32, 96,
 96, 11, 96, 11, 96,
 96, 32, 96, 11, 96]))