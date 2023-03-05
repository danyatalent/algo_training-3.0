n, m = map(int, input().split())
table = [list(map(int, input().split())) for i in range(n)]
for i in range(1, m):
    table[0][i] += table[0][i - 1]
for i in range(1, n):
    table[i][0] += table[i - 1][0]

for i in range(1, n):
    for j in range(1, m):
        table[i][j] += max(table[i - 1][j], table[i][j - 1])
print(table[n - 1][m - 1])
