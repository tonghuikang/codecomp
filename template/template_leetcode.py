import sys

m9 = 10**9 + 7  # 998244353
e18 = 10**18 + 10
MAXINT = sys.maxsize
abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c: i for i, c in enumerate(abc)}
d4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_neighbours(x, y, h, w):
    for dx, dy in d4:
        xx, yy = x + dx, y + dy
        if not (0 <= xx < h and 0 <= yy < w):
            continue
        yield xx, yy


# REMEMBER TO TAKE MODULO
