#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# ------------------------ standard imports ends here ------------------------

# to visualise graphs https://csacademy.com/app/graph_editor/


def build_graph(edges, bidirectional=False, costs=None):
    g = defaultdict(list)
    if costs:
        for (a,b),cost in zip(edges, costs):
            g[a].append((b,cost))
            if bidirectional:
                g[b].append((a,cost))
    else:
        for a,b in edges:
            g[a].append(b)
            if bidirectional:
                g[b].append(a)
    return g


def visit_accessible(map_from_node_to_nodes, start, visited=set()):
    # https://binarysearch.com/problems/Connected-Cities
    if not visited:
        visited = set()
    stack = [start]
    visited.add(start)
    while stack:
        cur = stack.pop()
        for nex in map_from_node_to_nodes[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            stack.append(nex)
    return visited


def count_connected_components_undirected(map_from_node_to_nodes, total_elements=0):
    # leetcode.com/problems/number-of-operations-to-make-network-connected
    visited = set()
    components = 0

    for node in map_from_node_to_nodes:
        if node in visited:
            continue
        visited = visit_accessible(map_from_node_to_nodes, start=node, visited=visited)
        components += 1
    if not total_elements:  # if all elements are already specified in the map
        return components
    
    return components + total_elements - len(map_from_node_to_nodes)


def dijkstra(list_of_indexes_and_costs, start):  # is it possible to do dijkstra directly?
    # leetcode.com/problems/path-with-maximum-probability/
    # leetcode.com/problems/network-delay-time/
    length = len(list_of_indexes_and_costs)
    visited = [False]*length
    weights = [MAXINT]*length
    path = [None]*length
    queue = []
    weights[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        g, u = heapq.heappop(queue)
        visited[u] = True
        for v, w in list_of_indexes_and_costs[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    heapq.heappush(queue, (f, v))
    return path, weights


def shortest_path_constant_cost(map_from_node_to_nodes, source, target):
    # to be tested
    # not a path
    d = map_from_node_to_nodes
    stack = deque([source])
    visited = {source: 0}
    while stack:
        cur = stack.popleft()
        for nex in d[cur]:
            if nex in visited:
                continue
            stack.append(nex)
            visited[nex] = visited[cur] + 1
            if nex == target:
                return visited[nex]
    return MAXINT


def dijkstra_with_preprocessing(map_from_node_to_nodes_and_costs, source, target, idxs=set()):
    # leetcode.com/problems/path-with-maximum-probability/
    # leetcode.com/problems/network-delay-time/
    d = map_from_node_to_nodes_and_costs

    if target not in d:  # destination may not have outgoing paths
        d[target] = []
    if source not in d:
        return MAXINT
    
    # assign indexes
    if idxs:
        idxs = {k:i for i,k in enumerate(idxs)}
    else:
        idxs = {k:i for i,k in enumerate(d.keys())}

    # populate list of indexes and costs
    list_of_indexes_and_costs = [[] for _ in range(len(idxs))]
    for e,vrr in d.items():
        for v,cost in vrr:
            list_of_indexes_and_costs[idxs[e]].append((idxs[v],cost))

    _, costs = dijkstra(list_of_indexes_and_costs, idxs[source])
    return costs[idxs[target]]


def floyd_warshall(map_from_node_to_nodes_and_costs, source, target, idxs=set()):
    raise NotImplementedError

class Dinic:
    # codeforces.com/contest/1473/submission/104332748
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# last = [-1 for i in range(101)]

# G = Dinic(n+2)

# res = 0
# for i in range(n):
#     if b[i] > 0:
#         res += b[i]
#         G.add_edge(i+1,n+1,b[i])
#     else:
#         G.add_edge(0,i+1,-b[i])

#     pre = last[a[i]]
#     if pre!=-1:
#         G.add_edge(pre+1,i+1,10**15)
#     for j in range(pre+1,i):
#         if a[i]%a[j]==0:
#             G.add_edge(j+1,i+1,10**15)

#     last[a[i]] = i

# print(res-G.flow(0,n+1))


def min_cost_flow(map_from_node_to_nodes_and_capcities, demands):
    raise NotImplementedError


class DisjointSet:
    # leetcode.com/problems/accounts-merge/
    def __init__(self, parent={}):
        if not parent:
            parent = {}
        self.parent = parent

    def find(self, item):
        if item not in self.parent:
            self.parent[item] = item
            return item
        elif self.parent[item] == item:
            return item
        else:
            res = self.find(self.parent[item])
            self.parent[item] = res
            return res

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2


def minimum_spanning_tree(edges, costs):
    # leetcode.com/problems/min-cost-to-connect-all-points
    if len(edges) == len(costs) == 0:
        return 0
    ds = DisjointSet()
    total_tree_cost = 0
    costs, edges = zip(*sorted(zip(costs, edges)))  # sort based on costs
    for cost, (u, v) in zip(costs, edges):
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            total_tree_cost += cost
    return total_tree_cost

# above function is not sufficient for the following question
# leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/


def topological_sort(map_from_node_to_nodes, all_nodes=set()):
    # leetcode.com/problems/course-schedule-ii/
    indegree_counter = defaultdict(int)
    for lst in map_from_node_to_nodes.values():
        for v in lst:
            indegree_counter[v] += 1

    if not all_nodes:  # assume all nodes are found in the map
        all_nodes = set(indegree_counter.keys()) | set(map_from_node_to_nodes)

    dq = deque([node for node in all_nodes if node not in indegree_counter])

    res = []
    while dq:
        cur = dq.popleft()
        res.append(cur)
        for nex in map_from_node_to_nodes[cur]:
            indegree_counter[nex] -= 1
            if indegree_counter[nex] == 0:
                dq.append(nex)
    return res if len(res) == len(all_nodes) else []


def detect_cycle(map_from_node_to_nodes):
    if not map_from_node_to_nodes:
        return False
    # leetcode.com/problems/course-schedule/
    return topological_sort(map_from_node_to_nodes) == []


def clique_cover(edges, N):
    # clique cover https://en.wikipedia.org/wiki/Clique_cover
    # https://atcoder.jp/contests/abc187/tasks/abc187_f
    # https://atcoder.jp/contests/abc187/submissions/19150883
    # the chromatic number is clique cover of the non-edges of the of the graph
    # https://codeforces.com/blog/entry/57496
    # https://codegolf.stackexchange.com/questions/37709/find-the-chromatic-number
    # to edit the following to follow the format, to understand what is going on also
    edges = set(tuple(edge) for edge in edges)
    ccs = [[1]]
    ret = 100
    
    def visit(pos):
        nonlocal ret
        # debug(pos, ccs, msg=":pos")
        if pos == N + 1:
            if len(ccs) < ret:
                ret = len(ccs)
                # debug(msg=":min")
            return
        if len(ccs) >= ret:
            # debug(msg=":early stop")
            return

        for cc in ccs:
            if all((v, pos) in edges for v in cc):
                # can join the cc
                cc.append(pos)
                visit(pos + 1)
                cc.pop()

        # create new cc
        # cid = len(ccs)
        ccs.append([pos])
        # vcc[pos - 1] = cid
        visit(pos + 1)
        ccs.pop()

    visit(2)
    return ret