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
