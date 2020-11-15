import sys
 
mod = 10**9 + 7
input = sys.stdin.readline
H, W = map(int, input().split())
grid = []
for i in range(H):
    grid.append(list(input().strip()))
dp = [0] * W
dp[0] = 1

dp = [[0] * (W+1) for _ in range(H+1)]
w_acc = [[0] * (W+1) for _ in range(H+1)]
h_acc = [[0] * (W+1) for _ in range(H+1)]
hw_acc = [[0] * (W+1) for _ in range(H+1)]
for i in range(1, H+1):
    if i == 1:
        dp[1][1] = 1
        w_acc[1][1] = 1
    for j in range(1, W+1):
        if grid[i-1][j-1] == "#":
            dp[i][j] = 0
            w_acc[i][j] = 0
            h_acc[i][j] = 0
            hw_acc[i][j] = 0
            continue
        dp[i][j] += h_acc[i-1][j] + hw_acc[i-1][j-1] + w_acc[i][j-1]

        w_acc[i][j] = w_acc[i][j-1] + dp[i][j]
        h_acc[i][j] = h_acc[i-1][j] + dp[i][j]
        hw_acc[i][j] = hw_acc[i-1][j-1] + dp[i][j]

        dp[i][j] %= mod
        w_acc[i][j] %= mod
        h_acc[i][j] %= mod
        hw_acc[i][j] %= mod

    # print(dp[i])

# print(dp)
# print(w_acc)
# print(h_acc)
# print(hw_acc)

print(dp[H][W])