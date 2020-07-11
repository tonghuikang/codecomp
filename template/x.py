a,b,c = list(map(int,input().split()))

res = 0
for i in range(a,b+1):
  if i%c == 0:
    res += 1

print(res)