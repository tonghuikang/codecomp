#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# ------------------------ standard imports ends here ------------------------


def build_graph(edges, bidirectional=False, costs=None):
    g = defaultdict(list)
    if costs:
        for (a,b),c in zip(edges, costs):
            g[a].append((b,c))
            if bidirectional:
                g[b].append((a,c))
    else:
        for a,b in edges:
            g[a].append(b)
            if bidirectional:
                g[b].append(a)
    return g


def visit_accessible(map_from_node_to_nodes, visited, start):
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


def count_connected_components_undirected(map_from_node_to_nodes):
    visited = set()
    components = 0

    for i in map_from_node_to_nodes:
        if i in visited:
            continue
        visit_accessible(map_from_node_to_nodes, visited=visited, start=i)
        components += 1
    return components


def dijkstra_with_preprocessing(map_from_node_to_nodes_and_costs, source, target):
    d = map_from_node_to_nodes_and_costs

    if target not in d:  # destination may not have outgoing paths
        d[target] = []
    if source not in d:
        return MAXINT
    
    # assign indexes
    idxs = {k:i for i,k in enumerate(d.keys())}

    # populate list of indexes and costs
    list_of_indexes_and_costs = [[] for _ in range(len(idxs))]
    for e,vrr in d.items():
        for v,cost in vrr:
            list_of_indexes_and_costs[idxs[e]].append((idxs[v],cost))

    _, costs = dijkstra(list_of_indexes_and_costs, idxs[source])
    return costs[idxs[target]]


def dijkstra(list_of_indexes_and_costs, start):  # is it possible to do dijkstra directly?
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


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True


class DisjointSet:
    def __init__(self, parent={}):
        self.parent = parent.copy()

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