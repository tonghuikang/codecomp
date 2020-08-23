import sys
import heapq as hq
import functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    weights = [math.inf]*n
    path = [None]*n
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return path, weights

def solve(edges, stones_available, recipies_target, recipies_ingredients, total_stones, total_junctions):  # fix inputs here
    edges = [(a-1, b-1) for a,b in edges]
    stones_available = [[a-1 for a in junction] for junction in stones_available]
    recipies_target = [x-1 for x in recipies_target]
    recipies_ingredients = [[a-1 for a in components] for components in recipies_ingredients]
    console("----- solving ------")
    console(edges)
    console(stones_available)
    console(recipies_target)
    console(recipies_ingredients)
    console(total_stones, total_junctions)
    console()
    # return a string (i.e. not a list or matrix)

    # stones-junction matrix of cost of availability
    # junction-junction matrix of distance
    # activate recipie until good

    # calculate distance matrix
    distance = [[None for _ in range(total_junctions)] for _ in range(total_junctions)]

    G = [[] for _ in range(total_junctions)]
    for a,b in edges:
        G[a].append((b,1))
        G[b].append((a,1))

    for start in range(total_junctions):
        distance[start] = dijkstra(G, start)[1]

    # console(np.array(distance))

    # intialise availability
    availability = [[10**12+1 for _ in range(total_stones)] for _ in range(total_junctions)]

    for i,lst in enumerate(stones_available):
        for stone in lst:
           availability[i][stone] = 0

    prev_availability = [[10**12+1 for x in row] for row in availability]

    while True:
        if prev_availability == availability:
            break
        prev_availability = [[x for x in row] for row in availability]
        for junction1 in range(total_junctions):
            for stone in range(total_stones):
                for junction2 in range(total_junctions):
                    availability[junction2][stone] = min(availability[junction2][stone], 
                                                        availability[junction1][stone] + distance[junction1][junction2])

        for junction,lst in enumerate(availability):
            for target, ingredients in zip(recipies_target, recipies_ingredients):
                availability[junction][target] = min(availability[junction][target], 
                                                     sum(availability[junction][ingredient] for ingredient in ingredients))

        if min(row[0] for row in availability) > 10**12 + 10:
            return -1
            
        console("availability")
        # console(np.array(availability))

    return min(row[0] for row in availability)
    # cases
    # produce the golden stone at a single junction

    # return ""  


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
    n,m,s,r = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    edges = []
    for _ in range(m):
        edges.append(list(map(int,input().split())))

    stones_available = []
    for _ in range(n):
        stones_available.append(list(map(int,input().split()))[1:])

    recipies_target = []
    recipies_ingredients = []
    for _ in range(r):
        lst = list(map(int,input().split()))
        recipies_target.append(lst[-1])
        recipies_ingredients.append(lst[1:-1])

    res = solve(edges, stones_available, recipies_target, recipies_ingredients, s, n)  # please change
    
    if res >= 10**12:
        res = -1
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
