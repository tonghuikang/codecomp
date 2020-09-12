import sys
N = int(input())


def machine_actual(mode, num):
    print("{} {}".format(mode, num),flush = True)
    if mode == "C":
        sys.exit()
    k = int(input())
    return k

# states
sett = set(range(1,N+1))
machine_counter = 0

def machine_simulated(mode, num):
    global machine_counter
    machine_counter = machine_counter + 1
    if mode == "A":
        cnt = 0
        for x in range(num, N+1, num):
            if x in sett:
                cnt += 1
        return cnt
    
    if mode == "B":
        cnt = 0
        for x in range(num, N+1, num):
            if x in sett:
                cnt += 1
                if x != X:
                    sett.remove(x)
        return cnt
    
    if mode == "C":
        if num == X:
            print(True)
        print(False)


machine = machine_actual

def brute_force(lst):
    for i in lst[::-1]:
        _ = machine("B", i)
        k = machine("A", i)
        if k == 1:
            res = machine("C", i)
            break
    res = machine("C", 1)

if N < 3000:
    brute_force(list(range(1,N+1))), sett

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
#           331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013
         ]
cutoff = primes[-1]

factors = []
for p in primes:
    a = machine("B", p)
    b = machine("A", p)
    if b != 0:
        factors.append(p)
factors

if factors != []:
    base = 1
    for f in factors:
        base = base*f
    candidates = list(range(base, N+1, base))
    brute_force(candidates)

if factors == []:
    large_primes = []
    sieve = [[] for _ in range(N+1)]
    for i in range(2,N+1):
        if sieve[i] == []:
            if i > cutoff:
                large_primes.append(i)
            for j in range(i,N+1,i):
                sieve[j].append(i)

def clear(lst):
    for i in lst[::-1]:
        k = machine("A", i)
        if k == 1:
            res = machine("C", i)
            break
    
def check(lst, expected_remaining):
    for i in lst[::-1]:
        _ = machine("B", i)
    remaining = machine("A", 1)
    if expected_remaining != remaining:
        clear(lst)

while len(large_primes) > 10:
    clearing_primes = large_primes[:len(large_primes)//2]
    large_primes = large_primes[len(large_primes)//2:]
    check(clearing_primes, len(large_primes) + 1)
    
brute_force(large_primes)  # +1 from [1]