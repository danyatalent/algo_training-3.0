n = int(input())
A = [0] * 5004
B = [0] * 5004
C = [0] * 5004
A[1] = B[1] = C[1] = A[2] = B[2] = C[2] = A[3] = B[3] = C[3] = 3601
dp = [0] * 5004
dp[1] = dp[2] = dp[3] = 0
for i in range(4, n + 4):
    a, b, c = map(int, input().split())
    A[i], B[i], C[i] = a, b, c

for i in range(4, n + 4):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i - 1], dp[i - 3] + C[i - 2])
print(dp[n + 3])