import sys

k = int(input())

if k == 2:
    print("First", flush=True)
    print("2 1 2 1", flush=True)
    k = int(input())
    sys.exit()


print("Second",flush = True)
lst = list(map(int,input().split()))

def solve(lst, n):
    def print(*args):
        pass
    pairs = [[] for _ in range(n)]

    for i,p in enumerate(lst, start=1):
        pairs[p-1].append(i)

    pairs = [sorted(pair) for pair in pairs]
    baseline = [pair[0] for pair in pairs]
    topline = [pair[1] for pair in pairs]
    variable = [pair[1] - pair[0] for pair in pairs]
    
    sum_baseline = sum(baseline)
    sum_variable = sum(variable)
    sum_topline = sum(topline)

    set_variable = set(variable)

    print(pairs)
    print("sum_baseline", sum_baseline)
    print("sum_variable", sum_variable)
    print("sum_variable", sum_topline)
    
    if sum_baseline%(2*n) == 0:
        return baseline
    
    if (sum_baseline + sum_variable)%(2*n) == 0:
        return topline
    
    for i in range(n):
        remainder = (2*n)*(1+sum_baseline//(2*n)) - sum_baseline
        print("remainder", remainder)
        if remainder in set_variable:
            idx = variable.index(remainder)
            baseline[idx] = topline[idx]
            return baseline

        overshoot = sum_topline - (2*n-i)*(sum_topline//(2*n))
        print("overshoot", overshoot)
        if overshoot in set_variable:
            idx = variable.index(overshoot)
            topline[idx] = baseline[idx]
            return topline

        baseline[i], topline[i] = topline[i], baseline[i]
        sum_baseline = sum_baseline + variable[i]
        sum_topline = sum_topline - variable[i]
        variable[i] = -variable[i]
    
    return baseline

res = solve(lst, k)
print(" ".join(str(x) for x in res))

k = int(input())
sys.exit()
