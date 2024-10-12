#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize


# ------------------------ geometry ------------------------


def shoelace_formula(xs, ys):
    # https://stackoverflow.com/a/30950874/5894029
    return sum(xs[i] * ys[i - 1] - xs[i - 1] * ys[i] for i in range(len(xs)))


def triangle_formula(xs, ys):
    # shoelace formula is 10x slower for some reason
    return (xs[0] * ys[1] + xs[1] * ys[2] + xs[2] * ys[0]) - (xs[0] * ys[2] + xs[1] * ys[0] + xs[2] * ys[1])


def get_polygon_area(xs, ys, take_abs=True, take_double=False):
    signed_area = shoelace_formula(xs, ys)  # switch to func=triangle_formula if needed for speed
    if not take_double:  # may cause precision issues idk
        signed_area = signed_area / 2
    if take_abs:
        return abs(signed_area)
    return signed_area


def checkStraightLine(coordinates):
    # https://leetcode.com/problems/check-if-it-is-a-straight-line/discuss/408984/
    (x0, y0), (x1, y1) = coordinates[:2]
    return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)


# ------------------------ standard imports ends here ------------------------


def ceiling_division(numer, denom):
    return -((-numer) // denom)


def lcm(a, b):
    # lowest common multiple
    return a * b // math.gcd(a, b)


# ------------------------ single prime factorisation ------------------------


def is_prime(n):
    # primality test (not tested)
    # https://github.com/not522/ac-library-python/blob/master/atcoder/_math.py
    # http://ceur-ws.org/Vol-1326/020-Forisek.pdf
    # untested
    if n <= 1:
        return False
    if n > 2**32:
        primitives = set([2, 325, 9375, 28178, 450775, 9780504, 1795265022])
        if n == 2:
            return True
    else:
        primitives = set([2, 7, 61])
        if n in primitives:
            return True

    if n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for a in primitives:
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0:
            return False
    return True


def get_prime_factors(nr):
    # factorize a single number into primes in O(sqrt(n))
    sqrt = math.sqrt(nr)
    i = 2
    factors = []
    while i <= nr:
        if i > sqrt:
            i = nr
        if (nr % i) == 0:
            factors.append(i)
            nr = nr // i
            sqrt = math.sqrt(nr)
        elif i == 2:
            i = 3
        else:
            i = i + 2
    return factors


def get_all_divisors_given_prime_factorization(factors):
    c = Counter(factors)

    divs = [1]
    for prime, count in c.most_common()[::-1]:
        l = len(divs)
        prime_pow = 1

        for _ in range(count):
            prime_pow *= prime
            for j in range(l):
                divs.append(divs[j] * prime_pow)

    # NOT IN SORTED ORDER
    return divs


# ---------------------- multiple prime factorisation ----------------------


def get_largest_prime_factors(num):
    # get largest prime factor for each number
    # you can use this to obtain primes
    largest_prime_factors = [1] * num
    for i in range(2, num):
        if largest_prime_factors[i] > 1:  # not prime
            continue
        for j in range(i, num, i):
            largest_prime_factors[j] = i
    return largest_prime_factors


SIZE_OF_PRIME_ARRAY = 10**6 + 10
largest_prime_factors = get_largest_prime_factors(SIZE_OF_PRIME_ARRAY)  # take care that it begins with [1,1,2,...]
primes = [x for i, x in enumerate(largest_prime_factors[2:], start=2) if x == i]


def get_prime_factors_with_precomp(num):
    # requires precomputed `largest_prime_factors``
    # for numbers below SIZE_OF_PRIME_ARRAY
    # O(log n)
    factors = []
    lf = largest_prime_factors[num]
    while lf != num:
        factors.append(lf)
        num //= lf
        lf = largest_prime_factors[num]
    if num > 1:
        factors.append(num)
    return factors


def get_prime_factors_with_precomp_sqrt(num):
    limit = int(num**0.5) + 2
    # requires precomputed `primes``
    # for numbers below SIZE_OF_PRIME_ARRAY**2
    # O(sqrt(n) / log(n))

    if num == 1:
        # may need to edit depending on use case
        return []

    factors = []
    for p in primes:
        while num % p == 0:
            factors.append(p)
            num = num // p
        # if num < p:  # remaining factor is a prime?
        #     break
        if p > limit:
            break
    if num > 1:
        # remaining number is a prime
        factors.append(num)

    return factors


# ----------------------------- modular inverse -----------------------------


# modular inverse
# https://stackoverflow.com/a/29762148/5894029
modinv = lambda A, n, s=1, t=0, N=0: (
    n < 2 and t % N or modinv(n, A % n, t, s - A // n * t, N or n),
    -1,
)[n < 1]


def modinv_p(base, p):
    # modular inverse if the modulo is a prime
    return pow(base, -1, p)  # for Python 3.8+
    # return pow(base, p-2, p)  # if Python version is below 3.8


def chinese_remainder_theorem(divisors, remainders):
    sum = 0
    prod = functools.reduce(lambda a, b: a * b, divisors)
    for n_i, a_i in zip(divisors, remainders):
        p = prod // n_i
        sum += a_i * modinv(p, n_i) * p
    return sum % prod


# --------------------- extended eucliean algorithm ---------------------


def extended_gcd(a, b):
    # Extended Euclidean Algorithm
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def solve_diophantine(a, b, n):
    # https://atcoder.jp/contests/abc315/submissions/44768509
    # Make sure that a and b are not both zero
    assert not (a == 0 and b == 0), "Both a and b cannot be zero"

    gcd, x, y = extended_gcd(a, b)

    # The equation has a solution only if n is a multiple of the gcd of a and b
    if n % gcd != 0:
        return False, 0, 0

    # Scale x and y by n/gcd
    x *= n // gcd
    y *= n // gcd

    # Check if the solution is correct
    assert a * x + b * y == n

    x2 = b // math.gcd(a, b)
    y2 = a // math.gcd(a, b)

    assert a * (x + x2) + b * (y - y2) == n

    return True, x, y


# ----------------------------- combinatorics  -----------------------------


LARGE = 2**20
p = 998244353  # CHANGE WHEN NEEDED

factorial_mod_p = [1]
for i in range(1, LARGE + 1):
    factorial_mod_p.append((factorial_mod_p[-1] * i) % p)

ifactorial_mod_p = [1] * (LARGE + 1)
ifactorial_mod_p[LARGE] = pow(factorial_mod_p[LARGE], p - 2, p)
for i in range(LARGE - 1, 1, -1):
    ifactorial_mod_p[i] = ifactorial_mod_p[i + 1] * (i + 1) % p


def ncr_mod_p(n, r, p=p):
    # https://codeforces.com/contest/1785/submission/192389526
    if r < 0 or n < r:
        return 0
    num = factorial_mod_p[n]
    dem = (ifactorial_mod_p[r] * ifactorial_mod_p[n - r]) % p
    return (num * dem) % p


# ----------------------------- counting  -----------------------------

from math import comb
from functools import cache


@cache
def count_numbers_with_certain_sum_of_digits_and_number_of_digits(n, k, mu=10):  # digit_sum, num_digits
    # https://math.stackexchange.com/a/1125403/353989
    limit = min(k, n // mu)
    total = 0

    for i in range(limit + 1):
        total += ((-1) ** i) * math.comb(k, i) * math.comb(n - mu * i + k - 1, k - 1)

    return total


@cache
def count_numbers_with_at_most_certain_sum_of_digits_and_number_of_digits(n, k):  # digit_sum, num_digits
    # includes 0
    # does not include 10**k
    if k == 0 or n == 0:
        return 1
    res = 0
    for n2 in range(n + 1):
        res += count_numbers_with_certain_sum_of_digits_and_number_of_digits(n2, k)
    return res


def count_numbers_with_at_most_certain_sum_of_digits(req_digit_sum, target):
    # https://leetcode.com/contest/weekly-contest-348/problems/count-of-integers/
    # You have a function (say from Stack Overflow) that calculates the value
    #   f(x, y) = f'(x, k), where y = 10**k is a power of 10
    # You want to find the value of f(x, y) where y may not be a power of 10
    # x may also be affected by the integer prefix
    # Note the requirements for f(x, y)

    x = str(target)
    res = 0
    remaining_digit_sum = req_digit_sum
    remaining_digits = len(x)

    for i, c in enumerate(x):
        c = int(c)
        remaining_digits -= 1
        for _ in range(c):
            if remaining_digit_sum < 0:
                break
            val = count_numbers_with_at_most_certain_sum_of_digits_and_number_of_digits(
                remaining_digit_sum, remaining_digits
            )
            res += val
            remaining_digit_sum -= 1

    return res


def generate_partitions(n):
    # https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B2
    # https://code.activestate.com/recipes/218332/

    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return
        
    # modify partitions of n-1 to form partitions of n
    for p in generate_partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]


@cache
def stirling2(n, k, m9):
    # https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
    # https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event
    # the number of ways to partition a set of n distinguishable objects into k non-empty subsets
    if n == k:
        return 1 % m9
    if n == 0 or k == 0:
        return 0
    return (k * stirling2(n-1, k) + stirling2(n-1, k-1)) % m9


# ----------------------------- floor sums  -----------------------------


def floor_sum_over_divisor(n, k, j):
    # https://math.stackexchange.com/questions/384520/efficient-computation-of-sum-k-1n-lfloor-fracnk-rfloor
    # https://mathoverflow.net/questions/48357/summation-of-a-series-of-floor-functions
    def floor_sum_over_divisor_(n, k, j):
        return sum(n // d for d in range(j + 1, k + 1))

    return floor_sum_over_divisor_(n, n // j, n // k) + k * (n // k) - j * (n // j)


def floor_sum_over_numerator(n: int, m: int, a: int, b: int) -> int:
    # https://atcoder.jp/contests/practice2/tasks/practice2_c
    # https://atcoder.github.io/ac-library/master/document_en/math.html
    # https://github.com/not522/ac-library-python/blob/master/atcoder/math.py

    assert 1 <= n
    assert 1 <= m

    ans = 0

    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m

    if b >= m:
        ans += n * (b // m)
        b %= m

    y_max = (a * n + b) // m
    x_max = y_max * m - b

    if y_max == 0:
        return ans

    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum_over_numerator(y_max, a, m, (a - x_max % a) % a)

    return ans


# ------------------------- linear algebra --------------------------


def matrix_multiply_mod(A, B, mod):
    # https://leetcode.cn/contest/weekly-contest-362/ranking/
    # yawn_sean
    n, m = len(A), len(A[0])
    p = len(B[0])
    ans = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                ans[i][k] += A[i][j] * B[j][k]
                ans[i][k] %= mod
    return ans

def matrix_power_mod(matrix, exponent, mod):
    # raise a square matrix to a certain power
    n = len(matrix)
    
    # create the identity matrix
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1

    # exponentiation by squaring
    while exponent > 0:
        if exponent % 2 == 1:
            result = matrix_multiply_mod(result, matrix, mod)
            exponent -= 1
        else:
            matrix = matrix_multiply_mod(matrix, matrix, mod)
            exponent //= 2

    return result


# ------------------------- FFT convolution -------------------------


def convolution(a, b):
    # https://atcoder.jp/contests/abc196/submissions/21089133

    ROOT = 3
    MOD = 998244353
    roots = [pow(ROOT, (MOD - 1) >> i, MOD) for i in range(24)]  # 1 の 2^i 乗根
    iroots = [pow(x, MOD - 2, MOD) for x in roots]  # 1 の 2^i 乗根の逆元

    def untt(a, n):
        # inplace modification
        for i in range(n):
            m = 1 << (n - i - 1)
            for s in range(1 << i):
                w_N = 1
                s *= m * 2
                for p in range(m):
                    a[s + p], a[s + p + m] = (a[s + p] + a[s + p + m]) % MOD, (a[s + p] - a[s + p + m]) * w_N % MOD
                    w_N = w_N * roots[n - i] % MOD

    def iuntt(a, n):
        # inplace modification
        for i in range(n):
            m = 1 << i
            for s in range(1 << (n - i - 1)):
                w_N = 1
                s *= m * 2
                for p in range(m):
                    a[s + p], a[s + p + m] = (a[s + p] + a[s + p + m] * w_N) % MOD, (
                        a[s + p] - a[s + p + m] * w_N
                    ) % MOD
                    w_N = w_N * iroots[i + 1] % MOD

        inv = pow((MOD + 1) // 2, n, MOD)
        for i in range(1 << n):
            a[i] = a[i] * inv % MOD

    la = len(a)
    lb = len(b)
    if min(la, lb) <= 50:
        if la < lb:
            la, lb = lb, la
            a, b = b, a
        res = [0] * (la + lb - 1)
        for i in range(la):
            for j in range(lb):
                res[i + j] += a[i] * b[j]
                res[i + j] %= MOD
        return res

    deg = la + lb - 2
    n = deg.bit_length()
    N = 1 << n
    a += [0] * (N - len(a))
    b += [0] * (N - len(b))
    untt(a, n)
    untt(b, n)
    for i in range(N):
        a[i] = a[i] * b[i] % MOD
    iuntt(a, n)
    return a[: deg + 1]


def convolution(f, g):
    # https://atcoder.jp/contests/abc196/submissions/26418619
    size = len(f) + len(g) - 1
    size = 1 << (size - 1).bit_length()
    f = np.fft.rfft(f, size)
    g = np.fft.rfft(g, size)
    f *= g
    f = np.fft.irfft(f, size)
    return np.rint(f).astype(np.int32)


def walsh_hadamard(my_freqs):
    # https://en.wikipedia.org/wiki/Fast_Walsh%E2%80%93Hadamard_transform
    # https://leetcode.com/problems/count-pairs-with-xor-in-a-range/discuss/1119975/
    my_max = len(my_freqs)

    # If our array's length is not a power of 2,
    # increase its length by padding zeros to the right
    if my_max & (my_max - 1):
        my_max = 2 ** (my_max.bit_length())

    if my_max > len(my_freqs):
        my_freqs.extend([0] * (my_max - len(my_freqs)))

    h = 2
    while h <= my_max:
        hf = h // 2
        for i in range(0, my_max, h):
            for j in range(hf):
                u, v = my_freqs[i + j], my_freqs[i + j + hf]
                my_freqs[i + j], my_freqs[i + j + hf] = u + v, u - v
        h *= 2
    return my_freqs


# -------------------- expression parsing basic --------------------


def basic_calculator(s):
    # Supports () */ +-
    # O(n^2) runtime
    # medium.com/@CalvinChankf/solving-basic-calculator-i-ii-iii-on-leetcode-74d926732437
    # leetcode.com/problems/basic-calculator-iii/ (premium)
    # binarysearch.com/problems/Calculator/editorials/2867853
    # cp-algorithms.com/string/expression_parsing.html
    # still looking for a generic parser that accepts more flexible rules
    # - parentheses, unary, precedence, direction of operations (could be right to left)
    if len(s) == 0:
        return 0
    stack = []
    sign = "+"
    num = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            num = num * 10 + int(c)

        if c == "(":
            # find the corresponding ")"
            pCnt = 0
            end = 0
            clone = s[i:]
            while end < len(clone):
                if clone[end] == "(":
                    pCnt += 1
                elif clone[end] == ")":
                    pCnt -= 1
                    if pCnt == 0:
                        break
                end += 1
            # do recursion to calculate the sum within the next (...)
            num = basic_calculator(s[i + 1 : i + end])
            i += end

        if i + 1 == len(s) or (c == "+" or c == "-" or c == "*" or c == "/"):
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack[-1] = stack[-1] * num
            elif sign == "/":
                stack[-1] = int(stack[-1] / float(num))
            sign = c
            num = 0
        i += 1

    return sum(stack)


# ------------------ expression parsing with eval ------------------


class Infix:
    # overloading an operator for use in python native eval()
    # https://code.activestate.com/recipes/384122/
    # codeforces.com/blog/entry/90980?#comment-794419
    # to change the order of operations, just put brackets maybe
    #   https://en.wikipedia.org/wiki/Operator-precedence_parser#Alternative_methods
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.func(other, x))

    def __or__(self, other):
        return self.func(other)


# defining hash function for 2-tuple
from random import randint

rand = lambda: randint(10**128, 10**256)
S = [rand() for _ in range(4)]
g = lambda x, salt1, salt2: x * salt1 + salt2
f = Infix(lambda x, y: g(x, S[0], S[1]) ^ g(y, S[2], S[3]))


# execution
# expr = (1+(2#3))
# eval(expr.replace('#', '|f|'))


# ------------------ expression parsing general ------------------


from typing import NamedTuple, Iterable, Callable, List, Union
import math
import operator


class Operator(NamedTuple):
    precedence: int
    is_left_associative: bool
    is_unary: bool
    operation: Callable


class Function(NamedTuple):
    arg_count: int
    operation: Callable


class TokenError(Exception):
    pass


StackItem = Union[str, Function, Operator]
Number = Union[float, int]


BINARY_OPERATORS = {
    "+": Operator(1, True, False, operator.add),
    "-": Operator(1, True, False, operator.sub),
    "*": Operator(2, True, False, operator.mul),
    "/": Operator(2, True, False, operator.truediv),  # use floordiv for int
    "%": Operator(2, True, False, operator.mod),
    "^": Operator(3, False, False, operator.pow),
    "&": Operator(4, False, False, operator.and_),
    "|": Operator(4, False, False, operator.or_),
}


UNARY_OPERATORS = {
    "+": Operator(4, False, True, operator.pos),
    "-": Operator(4, False, True, operator.neg),
    "~": Operator(4, False, True, operator.inv),
}


OPERATORS = {*BINARY_OPERATORS, *UNARY_OPERATORS}
TOKEN_DIVIDERS = OPERATORS | set("(),")


FUNCTIONS = {
    "modpow": Function(3, pow),
    "pow": Function(2, pow),
    "min": Function(2, min),
    "max": Function(2, max),
    "cos": Function(1, math.cos),
    "sin": Function(1, math.sin),
    "ln": Function(1, math.log),
    "exp": Function(1, math.exp),
    "inf": Function(0, lambda: math.inf),
    "true": Function(0, lambda: 1),
    "false": Function(0, lambda: 0),
}


def is_number(item: StackItem) -> bool:
    if not isinstance(item, str):
        return False
    try:
        float(item)
        return True
    except ValueError:
        return False


def str_to_number(token: str) -> Number:
    try:
        int(token)
        return int(token)
    except ValueError:
        return float(token)


def tokenize(data: str) -> Iterable[str]:
    group: List[str] = []

    for char in data:
        if char.isspace():
            continue
        if char in TOKEN_DIVIDERS:
            if group:
                yield "".join(group)
                group.clear()
            yield char
        else:
            group.append(char)

    if group:
        yield "".join(group)


def shunting_yard(tokens: Iterable[str]) -> Iterable[StackItem]:
    op_stack: List[StackItem] = []
    may_be_unary = True

    for token in tokens:
        if is_number(token):
            yield token
            may_be_unary = False
        elif token in FUNCTIONS:
            op_stack.append(FUNCTIONS[token])
        elif token == ",":
            continue
        elif token == "(":
            op_stack.append(token)
            may_be_unary = True
        elif token == ")":
            while op_stack[-1] != "(":
                yield op_stack.pop()
            op_stack.pop()
            if op_stack and isinstance(op_stack[-1], Function):
                yield op_stack.pop()
            may_be_unary = False
        elif token in OPERATORS:
            cur_op = UNARY_OPERATORS[token] if (may_be_unary and token in UNARY_OPERATORS) else BINARY_OPERATORS[token]
            while op_stack and isinstance(op_stack[-1], Operator):
                prev_op = op_stack[-1]
                if cur_op.precedence < prev_op.precedence or (
                    cur_op.precedence == prev_op.precedence and cur_op.is_left_associative
                ):
                    yield op_stack.pop()
                else:
                    break
            op_stack.append(cur_op)
            may_be_unary = True
        else:
            raise TokenError(f'token "{token}" is unknown')

    while op_stack:
        yield op_stack.pop()


def evaluate_rpn(items: Iterable[StackItem]) -> Number:
    num_stack: List[Number] = [0]

    for item in items:
        if isinstance(item, str):
            num_stack.append(str_to_number(item))
        elif isinstance(item, Function):
            arguments = reversed([num_stack.pop() for _ in range(item.arg_count)])
            num_stack.append(item.operation(*arguments))
        elif item.is_unary:
            num_stack.append(item.operation(num_stack.pop()))
        else:
            arguments = reversed([num_stack.pop(), num_stack.pop()])
            num_stack.append(item.operation(*arguments))

    return num_stack[-1]


def evaluate_expression(data: str) -> Number:
    # https://pastebin.com/69BmYyrf
    # communicated on binarysearch chat by https://binarysearch.com/@/C0R3
    raw_tokens = tokenize(data)
    rpn_tokens = shunting_yard(raw_tokens)
    result = evaluate_rpn(rpn_tokens)
    return result


# execution
# evaluate_expression("(3 + 4) * (5 - 6)")
# evaluate_expression("cos(1 + sin(ln(5) - exp(8))^2)")


# -------------------- sprague-grundy function --------------------


def mex(arr):
    arr = set(arr)
    i = 0
    while i in arr:
        i += 1
    return i


# https://cp-algorithms.com/game_theory/sprague-grundy-nim.html
# https://oeis.org/A002187
dawson_arr = [0, 1, 1]
for n in range(len(dawson_arr), 500):
    dawson_arr.append(mex([dawson_arr[n - 2]] + [dawson_arr[n - j - 3] ^ dawson_arr[j] for j in range(n - 2)]))
dawson_arr = [
    0,
    1,
    1,
    2,
    0,
    3,
    1,
    1,
    0,
    3,
    3,
    2,
    2,
    4,
    0,
    5,
    2,
    2,
    3,
    3,
    0,
    1,
    1,
    3,
    0,
    2,
    1,
    1,
    0,
    4,
    5,
    2,
    7,
    4,
    0,
    1,
    1,
    2,
    0,
    3,
    1,
    1,
    0,
    3,
    3,
    2,
    2,
    4,
    4,
    5,
    5,
    2,
    3,
    3,
    0,
    1,
    1,
    3,
    0,
    2,
    1,
    1,
    0,
    4,
    5,
    3,
    7,
    4,
    8,
    1,
    1,
    2,
    0,
    3,
    1,
    1,
    0,
    3,
    3,
    2,
    2,
    4,
    4,
    5,
    5,
    9,
    3,
    3,
    0,
    1,
    1,
    3,
    0,
    2,
    1,
    1,
    0,
    4,
    5,
    3,
    7,
    4,
    8,
    1,
    1,
    2,
    0,
    3,
    1,
    1,
    0,
    3,
    3,
    2,
    2,
    4,
    4,
    5,
    5,
    9,
]  # has period 34 after the first 52 elements

# ------------------------- other methods -------------------------


# get all combination of factors of an integer
# https://leetcode.com/problems/count-ways-to-make-array-with-product/
# https://www.geeksforgeeks.org/print-combinations-factors-ways-factorize/
