a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))

def solve(a,b,c,d):
    if a == c and b == d:
        return 0

    if abs(a-c) == abs(b-d):
        return 1
    
    if abs(a-c) + abs(b-d) <= 3:
        return 1

    if abs(abs(a-c) - abs(b-d)) <= 3:
        return 2

    if (a-c)%2 == (b-d)%2:
        return 2

    return 3

print(solve(a,b,c,d))

