def dfs(graph, visited, now, color):
    global Error
    visited[now] = color
    for neig in graph[now]:
        if visited[neig] == 0:
            dfs(graph, visited, neig, 3 - color)
        elif visited[now] == visited[neig]:
            Error = 1

            

n, m = map(int, input().split())
graph = {}
visited = [0] * (n + 1)

for i in range(1, n + 1):
    graph[i] = []

for i in range(m):
    lhs, rhs = map(int, input().split())
    graph[lhs] += [rhs]
    graph[rhs] += [lhs]

Error = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, visited, i, 1)
if Error:
    print('NO')
else:
    print('YES')