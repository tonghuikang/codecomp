def solve(a,b):
    # a = num_ranks
    # b = num_suits
    def print(*args):
        pass

    state = []
    for x in range(a):
        state.extend([(y, x) for y in range(b)])
    state = state

    print("init : ", state)

    res = 0
    seq = []
    
    while sorted([x[0] for x in state]) != [x[0] for x in state]:
        res += 1
        
        var = False
        # prev = state[-1]
        match = None
        start = 0
        end = -1
        for i,s in enumerate(state):
            if not var and i < a*(s[0]):
                var = True
                start = i
                match = state[i-1][0]
            elif var and match == s[0]:
                end = i
                xx, yy = a*b - end, end - start
                seq.append((xx, yy))
                break

        print(start, end, match, xx, yy)
        state = state[:start] + state[end:] + state[start:end]
        print(state)

        # if res > 10:
        #     break

    return res, seq


# print("2,2 : ", solve(2,2))
# print("2,3 : ", solve(2,3))
# print("3,2 : ", solve(3,2))

    
str_in = input()

for case in range(int(str_in)):
    strr = input()
    a,b = [int(x) for x in strr.split()]
    res, seq = solve(b,a)
    
    print("Case #{}: {}".format(case + 1, res))
    for a,b in seq:
        print("{} {}".format(a,b))

