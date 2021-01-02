p=lambda: tuple(map(int, input().split()))
n,k = p()
e = set()
for i in range(n):
    for j in range(i+1,n):
        e.add((i+1,j+1))
for _ in range(k):
    e.remove(p())
f=lambda n,e,m=1:any(all(t*m//m**a%m!=t*m//m**b%m for(a,b)in e)for t in range(m**n))and m or f(n,e,m+1)
print(f(n,e))