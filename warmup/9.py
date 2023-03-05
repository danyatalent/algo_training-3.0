n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]


partlyMatrix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        partlyMatrix[i][j] = partlyMatrix[i][j - 1] + partlyMatrix[i - 1][j] - partlyMatrix[i - 1][j - 1] + matrix[i - 1][j - 1]

# print(matrix)
# print(partlyMatrix)

while k != 0:
    x1, y1, x2, y2 = map(int, input().split())
    sum = partlyMatrix[x2][y2] - partlyMatrix[x1 - 1][y2] - partlyMatrix[x2][y1 - 1] + partlyMatrix[x1 - 1][y1 - 1]
    print(sum)
    k -= 1
