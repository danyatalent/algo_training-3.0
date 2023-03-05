MAX_SIZE = 1010
n = int(input())
num1 = list(map(int, input().split()))
m = int(input())
num2 = list(map(int, input().split()))

num1.insert(0,0)
num2.insert(0,0)
# print(*num1)
# print(*num2)

dp = [[0] * MAX_SIZE for _ in range (MAX_SIZE)]
stack = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if num1[i] == num2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

i, j = n, m
while i and j:
    if num1[i] == num2[j]:
        stack.append(num1[i])
        i -= 1
        j -= 1
    elif dp[i - 1][j] == dp[i][j]:
        i -= 1
    else:
        j -= 1

for i in range(len(stack)):
    print(stack.pop(), end=' ')