#!/usr/bin/env python3

# recursion template
# I wonder if this could be optimised further

# https://codeforces.com/blog/entry/80158?locale=en
from types import GeneratorType
def bootstrap(f, stack=[]):
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
