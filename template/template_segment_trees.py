# -------------------------- Segment Tree --------------------------
# https://atcoder.github.io/ac-library/master/document_en/segtree.html


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


class SegTree:
    # https://github.com/not522/ac-library-python/blob/master/atcoder/segtree.py
    def __init__(
        self,
        op: typing.Callable[[typing.Any, typing.Any], typing.Any],
        e: typing.Any,
        v: typing.Union[int, typing.List[typing.Any]],
    ) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

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

    def max_right(self, left: int, f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


class LazySegTree:
    # https://github.com/not522/ac-library-python/blob/master/atcoder/lazysegtree.py
    def __init__(
        self,
        op: typing.Callable[[typing.Any, typing.Any], typing.Any],
        e: typing.Any,
        mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
        composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
        id_: typing.Any,
        v: typing.Union[int, typing.List[typing.Any]],
    ) -> None:
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

    def apply(
        self,
        left: int,
        right: typing.Optional[int] = None,
        f: typing.Optional[typing.Any] = None,
    ) -> None:
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

    def max_right(self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
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


"""
Guides
- https://cp-algorithms.com/data_structures/segment_tree.html
- https://atcoder.github.io/ac-library/production/document_en/segtree.html
- https://atcoder.github.io/ac-library/production/document_en/lazysegtree.html
- https://atcoder.jp/contests/practice2/editorial
"""


"""
[SEGMENT TREE]
If there are range updates, you should use the Lazy Segment Tree instead.

The following should be defined.
- The type `S`
- The binary operation `S op(S a, S b)`
- The identity element `S e()`

Some explanation
- `op()` is used for the range queries
- `e()` in S is analogous to zero in the addition field in integers.
- `e()` in S is analogous to one in the multiplication field in integers.
- `op(a, e()) = op(e(), a) = op(a)` for all `a`


LONGEST SUBSTRING OF ONE REPEATING CHARACTER
# https://leetcode.com/problems/longest-substring-of-one-repeating-character/

e = -1, -1, -1, -1, True, True, 0
# left count, left value, right count, right value, is contiguous, is empty, max result

def op(left, right):
    lc1, lv1, rc1, rv1, contig1, empty1, mr1 = left
    lc2, lv2, rc2, rv2, contig2, empty2, mr2 = right

    if empty1 and empty2:
        return e
    if empty1:
        return right
    if empty2:
        return left

    if contig1 and contig2 and rv1 == lv2:
        return mr1 + mr2, lv1, mr1 + mr2, rv2, True, False, mr1 + mr2

    mr = max(mr1, mr2)
    if rv1 == lv2:
        mr = max(mr, rc1 + lc2)

        if contig1:
            return mr1 + lc2, lv1, rc2, rv2, False, False, mr

        if contig2:
            return lc1, lv1, rc1 + mr2, rv2, False, False, mr

    return lc1, lv1, rc2, rv2, False, False, mr

def init(val):
    return 1, val, 1, val, True, False, 1

st = SegTree(op, e, [init(x) for x in s])
res = []
st.set(idx, init(a))
st.prod(0, len(s))[-1]


MAJORITY ELEMENT OF AN SUBARRAY
# https://leetcode.com/problems/online-majority-element-in-subarray/
(Apparently need a Merge Sort Tree to solve this?)


RANGE SUM QUERIES WITH POINT UPDATES
# Basic example - sum over a range
# Use case: Given an array, answer queries for sum(arr[l:r]) efficiently

op = lambda a, b: a + b
e = 0

arr = [1, 2, 3, 4, 5]
st = SegTree(op, e, arr)
print(st.prod(1, 4))  # sum of arr[1:4] = 2+3+4 = 9
st.set(2, 10)         # set arr[2] = 10
print(st.prod(1, 4))  # sum of arr[1:4] = 2+10+4 = 16


RANGE MINIMUM/MAXIMUM QUERIES
# Query for minimum/maximum in a range

# For minimum queries
op = lambda a, b: min(a, b)
e = float('inf')

arr = [5, 2, 8, 1, 9, 3]
st = SegTree(op, e, arr)
print(st.prod(1, 5))  # min of arr[1:5] = min(2,8,1,9) = 1
st.set(3, 10)         # set arr[3] = 10
print(st.prod(1, 5))  # min of arr[1:5] = min(2,8,10,9) = 2

# For maximum queries
op = lambda a, b: max(a, b)
e = float('-inf')

arr = [5, 2, 8, 1, 9, 3]
st = SegTree(op, e, arr)
print(st.prod(1, 5))  # max of arr[1:5] = max(2,8,1,9) = 9


RANGE GCD QUERIES
# Query for GCD over a range
from math import gcd

op = lambda a, b: gcd(a, b)
e = 0

arr = [12, 18, 24, 36]
st = SegTree(op, e, arr)
print(st.prod(0, 3))  # gcd(12, 18, 24) = 6
st.set(1, 36)         # set arr[1] = 36
print(st.prod(0, 3))  # gcd(12, 36, 24) = 12


COUNTING INVERSIONS WITH UPDATES
# Count elements less than or equal to x in range [l, r)
# Store sorted list at each node, but this is more complex
# Better approach: use count in range with coordinate compression

# For a simpler version: count zeros in range
op = lambda a, b: a + b
e = 0

arr = [1, 0, 0, 1, 0, 1]  # 1 means non-zero, 0 means zero
st = SegTree(op, e, arr)
print(st.prod(1, 5))  # count zeros in arr[1:5] = 3
st.set(2, 1)          # set arr[2] = 1 (no longer zero)
print(st.prod(1, 5))  # count zeros in arr[1:5] = 2


BINARY SEARCH ON SEGMENT TREE - max_right
# Find the first index where a condition fails
# max_right(left, f) returns the maximum r such that f(prod(left, r)) is True
# Use case: Find the first position where cumulative sum >= target

op = lambda a, b: a + b
e = 0

arr = [3, 1, 4, 1, 5, 9, 2, 6]
st = SegTree(op, e, arr)

# Find first position from index 0 where cumsum >= 10
target = 10
pos = st.max_right(0, lambda x: x < target)
print(f"First position where cumsum >= {target}: {pos}")  # cumsum up to pos-1 is < 10
print(f"Cumulative sum at position {pos}: {st.prod(0, pos+1)}")

# Find first position from index 2 where cumsum >= 15
start = 2
cumsum_before = st.prod(0, start)
pos = st.max_right(start, lambda x: x + cumsum_before < 15)
print(f"First position from {start} where cumsum >= 15: {pos}")


BINARY SEARCH ON SEGMENT TREE - min_left
# Find the last index where a condition is true (searching backwards)
# min_left(right, f) returns the minimum l such that f(prod(l, right)) is True
# Use case: Find the leftmost position where sum from that position to right >= target

op = lambda a, b: a + b
e = 0

arr = [3, 1, 4, 1, 5, 9, 2, 6]
st = SegTree(op, e, arr)

# Find leftmost position where sum to index 7 >= 20
right = 7
target = 20
pos = st.min_left(right, lambda x: x < target)
print(f"Leftmost position where sum to {right} >= {target}: {pos}")
print(f"Sum from {pos} to {right}: {st.prod(pos, right+1)}")


FINDING K-TH ZERO (or any element)
# Find the k-th occurrence of a specific element
# Can be used to find k-th smallest, k-th zero, etc.

op = lambda a, b: a + b  # count zeros
e = 0

# Array where 1 means there's a zero at that position
arr = [1, 0, 1, 0, 1, 1, 0, 1]  # zeros at positions 0, 2, 4, 5, 7
st = SegTree(op, e, arr)

# Find position of 3rd zero (0-indexed, so k=3 means 4th zero)
k = 3
pos = st.max_right(0, lambda x: x <= k)
print(f"Position of {k+1}-th zero: {pos}")  # Should be position 5


FIRST ELEMENT GREATER THAN X IN RANGE
# Find first element > x in range [l, r)
# Store (max_value, index_of_max) at each node

op = lambda a, b: a if a[0] > b[0] else b
e = (float('-inf'), -1)

arr = [(val, idx) for idx, val in enumerate([3, 1, 4, 1, 5, 9, 2, 6])]
st = SegTree(op, e, arr)

# Find first element > 4 starting from index 2
start = 2
threshold = 4
pos = st.max_right(start, lambda x: x[0] <= threshold)
if pos < len(arr):
    print(f"First element > {threshold} from index {start}: value={arr[pos][0]} at pos={pos}")


RANGE MAX WITH INDEX
# Query for maximum value and its index in a range

op = lambda a, b: a if a[0] > b[0] else b
e = (float('-inf'), -1)

arr = [(val, idx) for idx, val in enumerate([3, 1, 4, 1, 5, 9, 2, 6])]
st = SegTree(op, e, arr)

max_val, max_idx = st.prod(2, 6)  # max in arr[2:6]
print(f"Max in range [2, 6): value={max_val} at index={max_idx}")
"""


"""
[LAZY SEGMENT TREE]
If there are range updates, you should use the Lazy Segment Tree

Conditions to apply Lazy Segment Tree
- $F$ contains the identity map $\mathrm{id}$, where the identity map is the map that satisfies $\mathrm{id}(x) = x$ for all $x \in S$.
- $F$ is closed under composition, i.e., $f \circ g \in F$ holds for all $f, g \in F$.
- $F$ is homomorphic, i.e. $f(x \cdot y) = f(x) \cdot f(y)$ holds for all $f \in F$ and $x, y \in S$.

You need to define the following
- The type `S` of the monoid
- The binary operation `S op(S a, S b)`
- The function `S e() -> S` that returns $e$
- The type `F` of the map
- The function `S mapping(F f, S x)` that returns $f(x)$
- The function `F composition(F f, F g)` that returns $f \circ g$
- The function `F id()` that returns $\mathrm{id}$

Some explanation
- `op()` is used for the range queries, `f` is used for the range updates
- `e()` in S is analogous to zero in the addition field in integers.
- `e()` in S is analogous to one in the multiplication field in integers.
- `op(a, e()) = op(e(), a) = op(a)` for all `a`
- `id` is an identity function in the range updates
- `id(x) = x` for all `x`
- `composition(id, f) = composition(f, id) = f`


RANGE NEGATION
x -> -x
# https://leetcode.cn/contest/biweekly-contest-98/problems/handling-sum-queries-after-update/

op = lambda a,b: a+b
e = 0
mapping = lambda f,x: f(x)
composition = lambda f,g: (lambda x: f(g(x)))
id_ = lambda x: x
f = lambda x: -x

st = LazySegTree(op, e, mapping, composition, id_, arr)
st.apply(l, r, f)   # l inclusive, r exclusive
st.prod(l, r)

However, the above code TLE in Python.
id_ and f is defined for every element in the array.
We can represent f and id_ as an integer instead, and let mapping execute the function

op = lambda a,b: a+b
e = 0
mapping = lambda f,x: f*x
composition = lambda f,g: f*g
id_ = 1
f = -1


RANGE ADDITION (not verified)
x -> a+x
# https://leetcode.com/contest/biweekly-contest-116/problems/subarrays-distinct-element-sum-of-squares-ii/

# (initial value, number of nodes
arr = [(0,1) for _ in range(len(nums))]

op = lambda a,b: (a[0]+b[0], a[1]+b[1])
e = 0,0
mapping = lambda f,x: (f*x[1] + x[0], x[1])
composition = lambda f,g: f+g
id_ = 0
f = 1

st = LazySegTree(op, e, mapping, composition, id_, arr)
st.apply(l, r, f)   # redefine f before calling this
st.prod(l, r)

We can avoid using functions to represent f and id_

op = lambda a,b: a+b
e = 0
mapping = lambda f,x: f+x
composition = lambda f,g: f+g
id_ = 0
f = a

st = LazySegTree(op, e, mapping, composition, id_, arr)
st.apply(l, r, f)   # redefine f before calling this
st.prod(l, r)

# but this does not work?

op = lambda a,b: a+b
e = 0
mapping = lambda f,x: f+x
composition = lambda f,g: f+g
id_ = 0
arr = [0,0,0]

st = LazySegTree(op, e, mapping, composition, id_, arr)
print(st.all_prod())
st.apply(0,3,100)
print(st.all_prod())

RANGE AFFINE TRANSFORM
x -> b*x + c
# https://github.com/not522/ac-library-python/blob/master/example/lazysegtree_practice_k_wo_modint.py

def op(x: Tuple[int, int], y: Tuple[int, int]) -> Tuple[int, int]:
    return (x[0] + y[0]) % mod, x[1] + y[1]
e = 0,0
def mapping(x: Tuple[int, int], y: Tuple[int, int]) -> Tuple[int, int]:
    return (x[0] * y[0] + x[1] * y[1]) % mod, y[1]
def composition(x: Tuple[int, int], y: Tuple[int, int]) -> Tuple[int, int]:
    return (x[0] * y[0]) % mod, (x[0] * y[1] + x[1]) % mod
id_ = 1,0
f = b,c

a = [(ai, 1) for ai in map(int, sys.stdin.readline().split())]
st = LazySegTree(op, e, mapping, composition, id_, a)
st.apply(l, r, (b, c))
st.prod(l, r)[0]

`f` can be different between queries.


RANGE SET/ASSIGNMENT WITH RANGE SUM QUERY
# Set all elements in range to a value, query for sum
# x -> c (set all elements to c)

# Store (sum, length) at each node
op = lambda a, b: (a[0] + b[0], a[1] + b[1])
e = (0, 0)

# mapping: apply value c to a segment of length len
mapping = lambda f, x: (f * x[1], x[1]) if f != float('inf') else x

# composition: later assignment overwrites earlier one
composition = lambda f, g: f if f != float('inf') else g

id_ = float('inf')  # special value meaning "no assignment"

arr = [(val, 1) for val in [1, 2, 3, 4, 5]]
st = LazySegTree(op, e, mapping, composition, id_, arr)

print(st.prod(0, 5)[0])  # sum = 1+2+3+4+5 = 15
st.apply(1, 4, 10)       # set arr[1:4] to 10
print(st.prod(0, 5)[0])  # sum = 1+10+10+10+5 = 36


RANGE SET TO MAXIMUM/MINIMUM
# Set all elements in range to max(current, x) or min(current, x)
# Useful for "raise floor" or "lower ceiling" operations

# For max(current, x)
op = lambda a, b: a + b
e = 0
mapping = lambda f, x: max(f, x) if f != float('-inf') else x
composition = lambda f, g: max(f, g)
id_ = float('-inf')

arr = [1, 5, 3, 7, 2, 8]
st = LazySegTree(op, e, mapping, composition, id_, arr)

print(st.prod(0, 6))    # sum = 26
st.apply(1, 5, 4)       # set all in [1,5) to max(current, 4)
# arr becomes [1, 5, 4, 7, 4, 8], elements < 4 become 4
print(st.prod(0, 6))    # sum = 29


RANGE INCREMENT WITH RANGE MINIMUM QUERY
# Increment range by value, query for minimum in range

# Store (min_value, count_of_min) for more complex queries if needed
# Simpler version: just store min_value
op = lambda a, b: min(a, b)
e = float('inf')
mapping = lambda f, x: x + f
composition = lambda f, g: f + g
id_ = 0

arr = [5, 2, 8, 1, 9, 3]
st = LazySegTree(op, e, mapping, composition, id_, arr)

print(st.prod(0, 6))    # min = 1
st.apply(1, 4, 3)       # add 3 to arr[1:4]
# arr becomes [5, 5, 11, 4, 9, 3]
print(st.prod(0, 6))    # min = 3


RANGE MULTIPLICATION WITH MODULO
# Multiply range by value (with modulo), query for sum with modulo
mod = 10**9 + 7

op = lambda a, b: (a + b) % mod
e = 0
mapping = lambda f, x: (x * f) % mod
composition = lambda f, g: (f * g) % mod
id_ = 1

arr = [1, 2, 3, 4, 5]
st = LazySegTree(op, e, mapping, composition, id_, arr)

print(st.prod(0, 5))    # sum = 15
st.apply(1, 4, 2)       # multiply arr[1:4] by 2
# arr becomes [1, 4, 6, 8, 5]
print(st.prod(0, 5))    # sum = 24


RANGE TOGGLE/FLIP (XOR WITH 1)
# Toggle/flip bits in a range
# Useful for: flipping 0s to 1s and vice versa

# Store (count_of_ones, length)
op = lambda a, b: (a[0] + b[0], a[1] + b[1])
e = (0, 0)

# mapping: f=1 means flip, f=0 means don't flip
# flipping: new_ones = length - old_ones
mapping = lambda f, x: (x[1] - x[0], x[1]) if f else x

# composition: flipping twice = no flip, XOR operation
composition = lambda f, g: f ^ g
id_ = 0  # no flip

arr = [(bit, 1) for bit in [1, 0, 1, 1, 0, 1]]
st = LazySegTree(op, e, mapping, composition, id_, arr)

print(st.prod(0, 6)[0])  # count of 1s = 4
st.apply(1, 5, 1)        # flip bits in [1, 5)
# arr becomes [1, 1, 0, 0, 1, 1]
print(st.prod(0, 6)[0])  # count of 1s = 4


RANGE BITWISE OR WITH RANGE QUERY
# Apply bitwise OR to a range, query for combined OR result
# mapping: f | x for each element

op = lambda a, b: a | b
e = 0
mapping = lambda f, x: x | f
composition = lambda f, g: f | g
id_ = 0

arr = [1, 2, 4, 8, 16]
st = LazySegTree(op, e, mapping, composition, id_, arr)

print(st.prod(0, 5))    # OR of all = 31
st.apply(1, 4, 3)       # OR each element in [1,4) with 3
# arr becomes [1, 3, 7, 11, 16]
print(st.prod(0, 5))    # OR of all = 31


LONGEST SUBSTRING OF ONE REPEATING CHARACTER
x -> y
# https://leetcode.com/problems/longest-substring-of-one-repeating-character/

e = -1, -1, -1, -1, True, True, 0

def op(left, right):
    # print(left)
    # print(right)
    # print()
    lc1, lv1, rc1, rv1, contig1, empty1, mr1 = left
    lc2, lv2, rc2, rv2, contig2, empty2, mr2 = right

    if empty1 and empty2:
        return e
    if empty1:
        return right
    if empty2:
        return left

    if contig1 and contig2 and rv1 == lv2:
        return mr1 + mr2, lv1, mr1 + mr2, rv2, True, False, mr1 + mr2

    mr = max(mr1, mr2)
    if rv1 == lv2:
        mr = max(mr, rc1 + lc2)

        if contig1:
            return mr1 + lc2, lv1, rc2, rv2, False, False, mr

        if contig2:
            return lc1, lv1, rc1 + mr2, rv2, False, False, mr

    return lc1, lv1, rc2, rv2, False, False, mr

def init(val):
    return 1, val, 1, val, True, False, 1

st = SegTree(op, e, [init(x) for x in s])
res = []
for a,idx in zip(queryCharacters, queryIndices):
    # print(a, idx)
    # print()
    st.set(idx, init(a))
    res.append(st.prod(0, len(s))[-1])


LONGEST BALANCED SUBSTRING
https://leetcode.com/problems/longest-balanced-subarray-ii//

def longestBalanced(self, nums: List[int]) -> int:
    # Monoid stores (sum, max_prefix_sum, min_prefix_sum)
    def op(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> Tuple[int, int, int]:
        s1, mp1, mn1 = a
        s2, mp2, mn2 = b
        s = s1 + s2
        mp = max(mp1, s1 + mp2)
        mn = min(mn1, s1 + mn2)
        return (s, mp, mn)

    e = (0, 0, 0)  # neutral: sum=0, max_pref=0, min_pref=0

    n = len(nums)
    st = SegTree(op, e, n)  # initial all zeros

    last = {}   # value -> last active index
    total = 0   # current total sum of the ±1/0 array (distinct evens - distinct odds)
    ans = 0

    # Helper to set a leaf with value w in {-1, 0, +1}
    def leaf(w: int) -> Tuple[int, int, int]:
        return (w, max(0, w), min(0, w))

    for i, v in enumerate(nums):
        sgn = 1 if (v % 2 == 0) else -1

        # Move the "last occurrence" marker for value v
        if v in last:
            st.set(last[v], e)  # old last is no longer last
        else:
            total += sgn  # first time seeing v, total changes

        st.set(i, leaf(sgn))
        last[v] = i

        # Find earliest x s.t. prefix sum D(x) = total
        # Then l = x + 1, and best length ending at i is i - l + 1 if l <= i.
        if total == 0:
            l = 0
        elif total > 0:
            # first x where D(x) >= total is where prefix max crosses total
            # use max_right with predicate mp < total
            x = st.max_right(0, lambda node: node[1] < total)
            l = x + 1
        else:
            # total < 0: first x where D(x) <= total is where prefix min crosses total
            # use max_right with predicate mn > total
            x = st.max_right(0, lambda node: node[2] > total)
            l = x + 1

        if l <= i:
            ans = max(ans, i - l + 1)

    return ans
"""


"""
[ADVANCED SEGMENT TREE VARIATIONS]

2D SEGMENT TREE
# For 2D range queries and updates
# Useful for: rectangle sum queries, rectangle min/max queries

# Basic structure: segment tree of segment trees
# Each node in the outer tree contains an inner segment tree

# Example: 2D range sum query
# Time: O(log²(n*m)) per query/update
# Space: O(n*m*log(n)*log(m))

class SegTree2D:
    def __init__(self, matrix):
        self.n = len(matrix)
        self.m = len(matrix[0]) if self.n > 0 else 0
        self.tree = [[0] * (4 * self.m) for _ in range(4 * self.n)]
        if self.n > 0 and self.m > 0:
            self._build_x(0, 0, self.n - 1, matrix)

    def _build_y(self, vx, lx, rx, vy, ly, ry, matrix):
        if ly == ry:
            if lx == rx:
                self.tree[vx][vy] = matrix[lx][ly]
            else:
                self.tree[vx][vy] = self.tree[2*vx+1][vy] + self.tree[2*vx+2][vy]
        else:
            my = (ly + ry) // 2
            self._build_y(vx, lx, rx, 2*vy+1, ly, my, matrix)
            self._build_y(vx, lx, rx, 2*vy+2, my+1, ry, matrix)
            self.tree[vx][vy] = self.tree[vx][2*vy+1] + self.tree[vx][2*vy+2]

    def _build_x(self, vx, lx, rx, matrix):
        if lx != rx:
            mx = (lx + rx) // 2
            self._build_x(2*vx+1, lx, mx, matrix)
            self._build_x(2*vx+2, mx+1, rx, matrix)
        self._build_y(vx, lx, rx, 0, 0, self.m - 1, matrix)

# Usage for 2D problems:
# - https://codeforces.com/contest/1658/problem/E
# - Rectangle sum queries with point updates
# - Finding maximum in a rectangle

# Note: For Python, 2D segment tree can be TLE. Consider:
# 1. Using Fenwick Tree (BIT) for 2D range sum (faster)
# 2. Using sparse table for static 2D range min/max
# 3. Coordinate compression to reduce memory


DYNAMIC SEGMENT TREE (Sparse Segment Tree)
# Only create nodes when needed - useful for large ranges with sparse updates
# Use case: range [0, 10^9] but only 10^5 updates

# Example: range sum with dynamic node creation
class DynamicSegTree:
    def __init__(self, L, R):
        self.L = L  # minimum possible index
        self.R = R  # maximum possible index
        self.tree = {}  # sparse storage: {node_id: value}
        self.left = {}  # {node_id: left_child_id}
        self.right = {}  # {node_id: right_child_id}
        self.node_counter = 0
        self.root = self._new_node()

    def _new_node(self):
        node_id = self.node_counter
        self.node_counter += 1
        self.tree[node_id] = 0
        return node_id

    def update(self, idx, val, node=None, L=None, R=None):
        if node is None:
            node, L, R = self.root, self.L, self.R
        if L == R:
            self.tree[node] += val
            return
        M = (L + R) // 2
        if idx <= M:
            if node not in self.left:
                self.left[node] = self._new_node()
            self.update(idx, val, self.left[node], L, M)
        else:
            if node not in self.right:
                self.right[node] = self._new_node()
            self.update(idx, val, self.right[node], M+1, R)
        self.tree[node] = self.tree.get(self.left.get(node, -1), 0) + \
                          self.tree.get(self.right.get(node, -1), 0)

    def query(self, l, r, node=None, L=None, R=None):
        if node is None:
            node, L, R = self.root, self.L, self.R
        if r < L or R < l:
            return 0
        if l <= L and R <= r:
            return self.tree[node]
        M = (L + R) // 2
        left_sum = self.query(l, r, self.left.get(node), L, M) if node in self.left else 0
        right_sum = self.query(l, r, self.right.get(node), M+1, R) if node in self.right else 0
        return left_sum + right_sum

# Usage:
st = DynamicSegTree(0, 10**9)
st.update(1000000, 5)
st.update(999999999, 3)
print(st.query(0, 10**9))  # sum = 8

# Use cases:
# - Coordinate compression alternative
# - Very large range [0, 10^18] with sparse updates
# - Problems with unknown maximum index


PERSISTENT SEGMENT TREE
# Keep all versions of the segment tree across updates
# Use case: Query "what was the sum in range [l,r] after the k-th update?"
#
# Key idea: only create new nodes for the path that changes
# Memory: O(n + q*log(n)) where q is number of updates
# Time: same as regular segment tree

class PersistentSegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = {}  # {(version, node): value}
        self.left = {}  # {(version, node): left_child}
        self.right = {}  # {(version, node): right_child}
        self.versions = [None]  # versions[i] = root of version i
        # Build version 0
        self._build(arr, 0, 0, 0, self.n - 1)

    def _build(self, arr, ver, node, L, R):
        if L == R:
            self.tree[(ver, node)] = arr[L]
            return
        M = (L + R) // 2
        self.left[(ver, node)] = 2 * node + 1
        self.right[(ver, node)] = 2 * node + 2
        self._build(arr, ver, 2*node+1, L, M)
        self._build(arr, ver, 2*node+2, M+1, R)
        self.tree[(ver, node)] = self.tree[(ver, 2*node+1)] + self.tree[(ver, 2*node+2)]

# This is a simplified skeleton. Full implementation requires more careful node management.
# Use cases:
# - Time-travel queries: "what was the array at time t?"
# - Functional programming: immutable data structures
# - Problems requiring history of operations


MERGE SORT TREE
# Store sorted arrays at each segment tree node
# Use case: count elements in range [l, r] that are <= k
# Each node stores sorted version of its range

class MergeSortTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [[] for _ in range(4 * self.n)]
        self._build(0, 0, self.n - 1, arr)

    def _build(self, node, L, R, arr):
        if L == R:
            self.tree[node] = [arr[L]]
            return
        M = (L + R) // 2
        self._build(2*node+1, L, M, arr)
        self._build(2*node+2, M+1, R, arr)
        # Merge the two sorted arrays
        self.tree[node] = sorted(self.tree[2*node+1] + self.tree[2*node+2])

    def query_count_leq(self, l, r, k, node=0, L=None, R=None):
        # Count elements in [l, r] that are <= k
        if L is None:
            L, R = 0, self.n - 1
        if r < L or R < l:
            return 0
        if l <= L and R <= r:
            # Binary search in sorted array
            from bisect import bisect_right
            return bisect_right(self.tree[node], k)
        M = (L + R) // 2
        return (self.query_count_leq(l, r, k, 2*node+1, L, M) +
                self.query_count_leq(l, r, k, 2*node+2, M+1, R))

# Usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6]
mst = MergeSortTree(arr)
print(mst.query_count_leq(1, 5, 4))  # count elements in arr[1:6] <= 4

# Use cases:
# - K-th smallest in range (binary search on answer)
# - Count elements in range [l, r] within value range [a, b]
# - https://leetcode.com/problems/online-majority-element-in-subarray/


SEGMENT TREE WITH LAZY PROPAGATION - INTERVAL ADDITION AND ASSIGNMENT
# Support both range add and range set operations
# Store two lazy tags: add_lazy and set_lazy

# When processing lazy tags:
# 1. If set_lazy is active, it overrides everything
# 2. Then apply add_lazy

# This is more complex as you need to handle composition carefully
# set_lazy has priority, then add_lazy is applied on top

# Composition rules:
# - set(x) then set(y) = set(y)
# - set(x) then add(y) = set(x+y)
# - add(x) then set(y) = set(y)
# - add(x) then add(y) = add(x+y)


SEGMENT TREE BEATS
# Advanced lazy propagation that can handle chmax/chmin operations
# Key idea: store (max, second_max, count_of_max, sum)

# Operations:
# 1. Range chmax(x): set all elements to max(arr[i], x)
# 2. Range chmin(x): set all elements to min(arr[i], x)
# 3. Range sum query

# This uses "segment tree beats" technique by breaking queries early
# Reference: https://codeforces.com/blog/entry/57319

# Use cases:
# - https://codeforces.com/problemset/problem/1290/E
# - Range assign min/max + range sum


IMPLICIT SEGMENT TREE FOR COORDINATE COMPRESSION
# When you have values in range [0, 10^9] but only 10^5 distinct values
# Alternative to explicit coordinate compression

# Similar to dynamic segment tree but with different use case
# Use when: large value range, sparse updates, don't want to coordinate compress
"""


# Possible range queries
# - sum
# - maximum, minimum
# - greatest common divisor, least common multiple
# - number of zeros, k-th zeros (or any other number?)
# - first element larger than q

# Possible updates
# - pointwise update/sum
# - rangewise sum, multiplication, ax+c
# - rangewise assign
# - (lazy propagation)

# Other types
# 2D segment tree
# Implict segment tree

# Give some examples
# - 2D Segment tree for https://codeforces.com/contest/1658/problem/E
#   - probably https://codeforces.com/contest/1658/submission/151178090

# Predefined monoid ops (defined once, not per call)
E = (0, 0, 0)
def OP(a, b):
    s1, mp1, mn1 = a
    s2, mp2, mn2 = b
    s = s1 + s2
    return (s, max(mp1, s1 + mp2), min(mn1, s1 + mn2))

# Predefined predicates for max_right (avoid per-iteration lambdas)
THRESH = 0
def _pred_max_prefix_below(node):
    # True while max_prefix < THRESH
    return node[1] < THRESH

def _pred_min_prefix_above(node):
    # True while min_prefix > THRESH
    return node[2] > THRESH

# Constant leaves for w in {-1, 0, +1}
# Index by w+1 to avoid dict lookups
LEAF = [
    (-1, 0, -1),  # w = -1
    ( 0, 0,  0),  # w =  0
    ( 1, 1,  0),  # w = +1
]

def longestBalancedSubarrayII(nums):
    n = len(nums)
    st = SegTree(OP, E, n)

    # Store input midway in the function (as requested)
    morvintale = nums[:]  # noqa: F841

    # Faster than dict for nums[i] up to 1e5
    max_val = max(nums) if n else 0
    last = [-1] * (max_val + 1)

    total = 0
    ans = 0

    # Bind methods to locals to cut attribute lookup cost in the loop
    st_set = st.set
    st_max_right = st.max_right

    global THRESH

    for i, v in enumerate(nums):
        # 1 if even else -1 (branchless)
        sgn = 1 - ((v & 1) << 1)

        prev = last[v]
        if prev != -1:
            st_set(prev, E)  # old last no longer active
        else:
            total += sgn     # new distinct value enters

        st_set(i, LEAF[sgn + 1])
        last[v] = i

        if total == 0:
            l = 0
        elif total > 0:
            THRESH = total
            r_star = st_max_right(0, _pred_max_prefix_below)  # maximal r s.t. max_prefix < THRESH
            l = r_star + 1
        else:
            THRESH = total
            r_star = st_max_right(0, _pred_min_prefix_above)  # maximal r s.t. min_prefix > THRESH
            l = r_star + 1

        if l <= i:
            cand = i - l + 1
            if cand > ans:
                ans = cand

    return ans