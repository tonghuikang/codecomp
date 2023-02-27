#!/usr/bin/env python3
import os
import sys
from io import BytesIO, IOBase
# sys.setrecursionlimit(300000)

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

# m9 = 10**9 + 7  # 998244353
# yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
# MAXINT = sys.maxsize
# e18 = 10**18 + 10
LARGE = 10**15

# if testing locally, print to terminal with a different color
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def minus_one(arr):
    return [x-1 for x in arr]

# ---------------------------- template ends here ----------------------------

import typing

def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


def _bsf(n: int) -> int:
    x = 0
    while n % 2 == 0:
        x += 1
        n //= 2

    return x


class LazySegTree:
    # https://github.com/not522/ac-library-python/blob/master/atcoder/lazysegtree.py
    def __init__(
            self,
            op: typing.Callable[[typing.Any, typing.Any], typing.Any],
            e: typing.Any,
            mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
            composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
            id_: typing.Any,
            v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self._e
        smr = self._e
        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def apply(self, left: int, right: typing.Optional[int] = None,
              f: typing.Optional[typing.Any] = None) -> None:
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(
            self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, g: typing.Any) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id



def solve_ref(n, k, arr, crr, hrr):
    # your solution here

    # dp on what is the last job on machine 2


    dp = [LARGE for _ in range(k+1)]
    # dp[machine_1][machine_2] last job
    dp[-1] = 0
    
    prev = -1
    for idx in arr:
        # log(dp)
        # log(hrr)

        new_dp = [x + crr[idx] for x in dp]
        # new_dp.append(LARGE)
        new_dp[idx] = min(min(dp) + crr[idx], dp[idx] + hrr[idx])
        if prev != -1:
            new_dp[prev] = min(new_dp[prev], dp[idx] + hrr[idx])

        # log(idx, crr[idx], hrr[idx], dp, new_dp)
        dp = new_dp
        prev = idx

    
    return min(dp)


def solve_ref2(n, k, arr, crr, hrr):
    # your solution here

    # dp on what is the last job on machine 2

    dp = [LARGE for _ in range(k+1)]
    # dp[machine_1][machine_2] last job
    dp[k] = 0

    prev = k
    for idx in arr:
        # log(dp)
        # log(hrr)

        new_dp = [x + crr[idx] for x in dp]
        # new_dp.append(LARGE)
        new_dp[idx] = min(min(dp) + crr[idx], dp[idx] + hrr[idx])
        new_dp[prev] = min(new_dp[prev], dp[idx] + hrr[idx])

        # log(idx, crr[idx], hrr[idx], dp, new_dp)
        dp = new_dp
        prev = idx

    
    return min(dp)


def solve_(n, k, arr, crr, hrr):
    # your solution here

    # dp on what is the last job on machine 2

    # dp = [LARGE for _ in range(k+1)]
    # dp[machine_1][machine_2] last job
    # dp[-1] = 0

    # RANGE ADDITION (not verified)
    # x -> a+x
    # We could use Fenwick Tree for this, but let us try using LST

    op = lambda a,b: min(a,b)
    e = LARGE
    mapping = lambda f,x: f+x
    composition = lambda f,g: f+g
    id_ = 0

    dp = [LARGE for _ in range(k)]
    dp.append(0)
    st = LazySegTree(op, e, mapping, composition, id_, dp)
    # st.apply(l, r, f)   # redefine f before calling this
    # st.prod(l, r)

    # We can avoid using functions to represent f and id_

    # op = lambda a,b: a+b
    # e = 0
    # mapping = lambda f,x: f+x
    # composition = lambda f,g: (lambda x: f(g(x)))
    # id_ = 0
    # f = a

    # st = LazySegTree(op, e, mapping, composition, id_, arr)
    # st.apply(l, r, f)   # redefine f before calling this
    # st.prod(l, r)

    prev = k
    for idx in arr:
        # log(dp)

        # new_dp = [x + crr[idx] for x in dp]
        # log(idx, crr)
        f = crr[idx]

        # new_dp[idx] = min(min(dp) + crr[idx], dp[idx] + hrr[idx])
        min_dp = st.all_prod()
        dp_idx = st.get(idx)
        new_dp_idx = min(min_dp + crr[idx], dp_idx + hrr[idx])

        st.apply(0, k+1, f)
        st.set(idx, new_dp_idx)

        # new_dp[prev] = min(new_dp[prev], dp[idx] + hrr[idx])
        dp_prev = st.get(prev)
        new_dp_prev = min(dp_prev, dp_idx + hrr[idx])
        st.set(prev, new_dp_prev)

        # dp = new_dp
        prev = idx

    return st.all_prod()


allres = []

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    crr = list(map(int,input().split()))
    hrr = list(map(int,input().split()))
    arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    arr2 = []
    base_res = 0
    prev = -1
    for x in arr:
        if x == prev:
            base_res += hrr[x]
            continue
        arr2.append(x)
        prev = x
    arr = arr2
    # log(base_res)
    # log(arr)

    res = solve(n, k, arr, crr, hrr)  # include input here

    res += base_res

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    allres.append(str(res))

print("\n".join(allres))