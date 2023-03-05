n, m = map(int, input().split())
MAX = 55
dp = [[0] * MAX for _ in range(MAX)]
dp[1][1] = 1
for i in range(2, n + 1):
    for j in range(2, m + 1):
        dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j - 2]
print(dp[n][m])