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
