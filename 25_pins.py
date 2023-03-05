dp = [0] * 101
n = int(input())
cords = [0] * (n + 1)
s = input().split()
for i in range(1, n + 1):
    cords[i] = int(s[i - 1])
cords.sort()
dp[2] = cords[2] - cords[1]
if n > 3:
    dp[3] = cords[3] - cords[1]
    for i in range(4, n + 1):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cords[i] - cords[i - 1]
print(dp[n])
