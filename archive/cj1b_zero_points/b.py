def solve(A,B):
    # a = num_ranks
    # b = num_suits
    def print(*args):
        pass

    print(A,B)
    a = abs(A)
    b = abs(B)

    abin = list(bin(a))[2:][::-1]
    abin = [int(x) for x in abin]
    bbin = list(bin(b))[2:][::-1]
    bbin = [int(x) for x in bbin]

    print("abin, bbin", abin, bbin)

    if sum([int(x) for x in abin]) == 1 or A == 0:
        alt_abin = -1
    else:
        negabin = (2**len(abin)) - int(a)
        abin2 = list(bin(negabin)[2:][::-1])
        alt_abin = [0 for _ in range(len(abin)+1)]
        alt_abin[-1] = 1
        for i,b in enumerate(abin2):
            alt_abin[i] = -1

    if sum([int(x) for x in bbin]) == 1 or B == 0:
        alt_bbin = -1
    else:
        print(2**len(bbin), b)
        negbbin = (2**len(bbin)) - int(b)
        bbin2 = list(bin(negbbin)[2:][::-1])
        alt_bbin = [0 for _ in range(len(bbin)+1)]
        alt_bbin[-1] = 1
        for i,b in enumerate(bbin2):
            alt_bbin[i] = -1

    print("alt_abin, alt_bbin", alt_abin, alt_bbin)
    
    res = "IMPOSSIBLE"
    minlen = 10**9
        
    for aa in [abin, alt_abin]:
        if aa == -1:
            continue
        if A < 0:
            aa = [-a for a in aa]

        for bb in [bbin, alt_bbin]:
            if bb == -1:
                continue
            if B < 0:
                bb = [-b for b in bb]

            for i in range(max(len(aa), len(bb))):
                if i >= len(aa):
                    if abs(bb[i]) != 1:
                        break
                elif i >= len(bb):
                    if abs(aa[i]) != 1:
                        break
                elif abs(aa[i]) + abs(bb[i]) != 1:
                    break
            else:
                arr = ["" for _ in range(max(len(aa), len(bb)))]
                if len(arr) > minlen:
                    continue
                for i,a in enumerate(aa):
                    if a == -1:
                        arr[i] = "S"
                    if a == 1:
                        arr[i] = "N"
                for i,b in enumerate(bb):
                    if b == -1:
                        arr[i] = "W"
                    if b == 1:
                        arr[i] = "E"
                print(aa, bb, arr)
                minlen = len(arr)
                res = "".join(arr)

    return res


# print("2,2 : ", solve(2,2))
# print("2,3 : ", solve(2,3))
# print("3,2 : ", solve(3,2))

    
str_in = input()

for case in range(int(str_in)):
    strr = input()
    a,b = [int(x) for x in strr.split()]
    res = solve(b,a)
    
    print("Case #{}: {}".format(case + 1, res))

