n, m = map(int, input().split())
table = [list(map(int, input().split())) for i in range(n)]
for i in range(1, m):
    table[0][i] += table[0][i - 1]
for i in range(1, n):
    table[i][0] += table[i - 1][0]

for i in range(1, n):
    for j in range(1, m):
        table[i][j] += max(table[i - 1][j], table[i][j - 1])
stack = []
i, j = n - 1, m - 1

while i != 0 or j != 0:
    if i != 0 and j != 0:
        if table[i - 1][j] > table[i][j - 1]:
            stack.append('D')
            i -= 1
        else:
            stack.append('R')
            j -= 1
    elif i == 0 and j != 0:
        stack.append('R')
        j -= 1
    elif j == 0 and i != 0:
        stack.append('D')
        i -= 1
print(table[n - 1][m - 1])
for i in range(len(stack)):
    print(stack.pop(), end=' ')