#!/usr/bin/env python3

# usually, there is a great deal of overhead involved in recursion
# this usually results in exceeding time limit and memory limit
# these are some remedies

# recursion template
# I wonder if this could be optimised further

# https://codeforces.com/blog/entry/80158?locale=en
from types import GeneratorType
def bootstrap(f, stack=[]):
    # usage - please remember to YIELD to call and return
    # protip - do not store data structures in the function
    '''
    @bootstrap
    def recurse(n):
        if n <= 0:
            yield 0
        yield (yield recurse(n-1)) + 2

    res = recurse(10**5)
    '''
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    if stack:
                        stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


@bootstrap
def recurse(n):
    if n <= 0:
        yield 0
    yield (yield recurse(n-1)) + 2

# custom invocation with https://codeforces.com/problemset/customtest
value = int(input())
print(recurse(value))


# Python 3.7.2
# 10000000 Invocation failed [MEMORY_LIMIT_EXCEEDED]
# 3000000 Invocation failed [MEMORY_LIMIT_EXCEEDED]
# 1000000 Used: 2870 ms, 416360 KB
# 300000 Used: 842 ms, 130716 KB
# 100000 Used: 265 ms, 48336 KB

# PyPy 3.6
# 10000000 Invocation failed [MEMORY_LIMIT_EXCEEDED]
# 3000000 Used: 1964 ms, 505132 KB
# 1000000 Used: 748 ms, 182128 KB
# 300000 Used: 342 ms, 71108 KB
# 100000 Used: 233 ms, 48628 KB

# -----------------------------------------------------------------------------

# recusion template that does not use bootstrap
# for speed and memory reference
import sys, threading
threading.stack_size(2**27)
sys.setrecursionlimit(10**6 + 5)


def recurse(n):
    if n <= 0:
        return 0
    return recurse(n-1) + 2

# custom invocation with https://codeforces.com/problemset/customtest
def main():
    value = int(input())
    print(recurse(value))

t = threading.Thread(target=main)
t.start()
t.join()


# Python 3.7.2
# 1000000 Runtime error
# 500000 Used: 311 ms, 313180 KB
# 300000 Used: 234 ms, 243096 KB
# 100000 Used: 124 ms, 173080 KB

# PyPy 3.6
# 300000 Invocation failed [MEMORY_LIMIT_EXCEEDED]
# 100000 Used: 280 ms, 361072 KB
# with sys.setrecursionlimit(10**5 + 5)


# -----------------------------------------------------------------------------

# recusion template that does not use recursion

def not_dfs(start, g, entry_operation, exit_operation):
    # g is map of node to nodes
    # not dfs because it checks all the edges on entering
    # https://codeforces.com/contest/1646/submission/148435078
    # https://codeforces.com/contest/1656/submission/150799881
    entered = set([start])
    exiting = set()
    stack = [start]
    prev = {}

    null_pointer = "NULL"
    prev[start] = null_pointer

    while stack:
        cur = stack[-1]

        if cur not in exiting:
            for nex in g[cur]:
                if nex in entered:
                    continue

                entry_operation(prev[cur], cur, nex)

                entered.add(nex)
                stack.append(nex)
                prev[nex] = cur
            exiting.add(cur)

        else:
            stack.pop()
            exit_operation(prev[cur], cur)


def dfs(start, g, entry_operation, exit_operation):
    # g is map of node to nodes
    # assumes g is bidirectional
    # https://codeforces.com/contest/1714/submission/166648312
    entered = set([start])
    exiting = set()
    ptr = {x:0 for x in g}
    stack = [start]
    prev = {}

    null_pointer = "NULL"
    # might be faster to use an integer for null_pointer
    # especially if you avoid string compare when checking if null pointer
    # leaving as a string for safety reasons
    prev[start] = null_pointer

    while stack:
        cur = stack[-1]

        if cur not in exiting:
            while ptr[cur] < len(g[cur]):
                nex = g[cur][ptr[cur]]
                ptr[cur] += 1
                if nex in entered:
                    continue

                entry_operation(prev[cur], cur, nex)

                entered.add(nex)
                stack.append(nex)
                prev[nex] = cur
                break
            if ptr[cur] == len(g[cur]):
                exiting.add(cur)

        else:
            stack.pop()
            exit_operation(prev[cur], cur)


def entry_operation(prev, cur, nex):
    # note that prev is `null_pointer` at the root node
    pass

def exit_operation(prev, cur):
    pass
