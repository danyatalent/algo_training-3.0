n = int(input())
letters = [0] * (n + 1)
for i in range(n):
    letters[i] = int(input())
ans = 0
for i in range(n - 1):
    ans += min(letters[i], letters[i + 1])
print(ans)