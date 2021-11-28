from itertools import combinations
import numpy as np
import sys

def complement(bits): return [
    '_' if b=='_' else
    '1' if b=='0' else '0'
    for b in bits
]

class QuantumArray():
    def __init__(self, B):
        self.bits = ['_'] * B
        self.unkowns = list(range(B))
        self.read(10)
        self.run()

    def read(self, n):
        for _ in range(n):
            i = self.unkowns.pop()
            self.bits[i] = self.read_bit(i+1)
            self.unkowns = self.unkowns[::-1]
        self.update_states()

    def read_bit(self, i):
        interactive_print(i)
        return interactive_read()

    def update_states(self):
        self.bits_c  = complement(self.bits)
        self.bits_cr = self.bits_c[::-1]
        self.bits_r  = complement(self.bits_cr)
        self.states = [self.bits, self.bits_c, self.bits_cr, self.bits_r]

    def get_test_idx(self):
        candidates = list(set(range(B)) - set(self.unkowns))
        max_states = len(set(map(tuple, self.states)))
        for idx in combinations(candidates, 2):
            num_states = len(set(
                tuple(np.take(state, idx))
                for state in self.states
            ))
            if num_states == max_states: return idx

    def collapse(self):
        test_idx = self.get_test_idx()
        test = [self.read_bit(i+1) for i in test_idx]

        self.bits = next(state
            for state in self.states
            if test == list(np.take(state, test_idx))
        )

    def run(self):
        while True:
            self.collapse()
            try: self.read(8)
            except IndexError: break


def console(*args):  # the judge will not read these standard error output
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

def interactive_print(output):
    # print output with flush (and also print output to standard error)
    print(output, flush=True)
    print('\033[35m', output, '\033[0m', file=sys.stderr)


def interactive_read():
    # read (and also print input to standard error)
    input_string = input()
    print('\033[34m', input_string, '\033[0m', file=sys.stderr)
    return input_string


T, B = map(int, input().split())
for _ in range(T):
    array = QuantumArray(B)
    interactive_print(''.join(array.bits))
    if interactive_read() == 'N': sys.exit()
