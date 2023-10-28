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
