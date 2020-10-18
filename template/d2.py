t=int(input())
N=10
dp=[[0 for i in range(N+1)] for i in range(N+1)]
dp[2][1],dp[2][2]=1,1
for i in range(3,N+1):
    for j in range(1,i+1):
        dp[i][j] = 1/(i-1) + (j-1)/(i-1)*dp[i-1][max(1,j-1)] + (i-j)/(i-1)*dp[i-1][min(j,i-1)]
        if j>1 and j<i:
            dp[i][j] += 1/(i-1)

print(dp)

for tc in range(1,t+1):
    n=int(input())
    l=list(map(int,input().split(' ')))

    ans=0
    for i in range(1,n+1):
        ans+=dp[n][i]*l[i-1]

    print("Case #{}: {}".format(tc,ans))