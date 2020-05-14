def solve(n,k):

    if n%2 == 0:
        return n + k*2

    for i in range(3, 3000):
        if n%i == 0:
            fn = i
            break
    else:
        fn = n
        
    return n + (k-1)*2 + fn

strr = input()
for _ in range(int(strr)):
    strr = input()
    n,k = [int(x) for x in strr.split()]
    print(solve(n,k))
