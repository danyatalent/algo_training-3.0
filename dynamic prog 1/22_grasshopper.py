n, k = map(int, input().split())
dp = [0] * 36
dp[1], dp[2] = 1, 1
if n > 2:
    if k == 1:
        print(1)
    else:
        for i in range(3, k + 1):
            dp[i] = 2 * dp[i - 1]
        if n > k:
            for i in range(k + 1, n + 1):
                dp[i] = 2 * dp[i - 1] - dp[i - k - 1]
        print(dp[n])
else:
    print(dp[n])