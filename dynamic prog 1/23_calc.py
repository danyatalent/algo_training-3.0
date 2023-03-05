n = int(input())
dp = [0] * (10 ** 6 + 1)
dp[1], dp[2], dp[3] = 0, 1, 1
nums = []
if n > 3:
    for i in range(4, n + 1):
        if i % 2 == 0 and i % 3 == 0:
            dp[i] = min(dp[i - 1], dp[i // 3] + 1, dp[i // 2] + 1)
        elif i % 2 == 0 and i % 3 != 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        elif i % 2 != 0 and i % 3 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 3] + 1)
        else:
            dp[i] = dp[i - 1] + 1
i = n
while i != 1:
    if dp[i] == dp[i - 1] + 1:
        nums.insert(0, i)
        i -= 1
        continue
    if i % 2 == 0 and dp[i] == dp[i // 2] + 1:
        nums.insert(0, i)
        i //= 2
        continue
    nums.insert(0, i)
    i //= 3
nums.insert(0, 1)
print(dp[n])
print(*nums)