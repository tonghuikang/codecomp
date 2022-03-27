# https://codeforces.com/blog/entry/82989
# Some code to make your Python code run faster

import os
import sys
from io import BytesIO, IOBase
sys.setrecursionlimit(300000)

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



# the following may no longer be applicable as pypy3 is available as 64-bit
import __pypy__

int_add = __pypy__.intop.int_add
int_sub = __pypy__.intop.int_sub
int_mul = __pypy__.intop.int_mul


def make_mod_mul(mod=10**9 + 7):
    fmod_inv = 1.0 / mod

    def mod_mul(a, b, c=0):
        res = int_sub(int_add(int_mul(a, b), c), int_mul(mod, int(fmod_inv * a * b + fmod_inv * c)))
        if res >= mod:
            return res - mod
        elif res < 0:
            return res + mod
        else:
            return res

    return mod_mul


mod_mul = make_mod_mul()


def mod_pow(x, y):
    if y == 0:
        return 1
    res = 1
    while y > 1:
        if y & 1 == 1:
            res = mod_mul(res, x)
        x = mod_mul(x, x)
        y >>= 1
    return mod_mul(res, x)