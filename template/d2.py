import sys
import numpy as np

R,G,B=map(int,input().split())
r=list(map(int,input().split()))
g=list(map(int,input().split()))
b=list(map(int,input().split()))
r.sort()
g.sort()
b.sort()

def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

dp=[[[0 for i in range(B+1)] for j in range(G+1)] for i in range(R+1)]
 
for i in range(1,R+1):
    for j in range(1,G+1):
        dp[i][j][0]=dp[i-1][j-1][0]+r[i-1]*g[j-1]
 
for j in range(1,G+1):
    for k in range(1,B+1):
        dp[0][j][k]=dp[0][j-1][k-1]+b[k-1]*g[j-1]
 
for i in range(1,R+1):
    for k in range(1,B+1):
        dp[i][0][k]=dp[i-1][0][k-1]+r[i-1]*b[k-1]
 
console(np.array(dp))

for i in range(1,R+1):
    for j in range(1,G+1):
        for k in range(1,B+1):
            if max(r[i-1],g[j-1],b[k-1])==r[i-1]:
                dp[i][j][k]=max(dp[i-1][j-1][k]+r[i-1]*g[j-1],dp[i-1][j][k-1]+r[i-1]*b[k-1])
            elif max(r[i-1],g[j-1],b[k-1])==g[j-1]:
                dp[i][j][k]=max(dp[i-1][j-1][k]+r[i-1]*g[j-1],dp[i][j-1][k-1]+g[j-1]*b[k-1])
            else:
                dp[i][j][k]=max(dp[i][j-1][k-1]+b[k-1]*g[j-1],dp[i-1][j][k-1]+r[i-1]*b[k-1])
 
console(np.array(dp))

print(dp[R][G][B])
