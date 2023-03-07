def dfs(graph, visited, now, ans):
    global flag
    visited[now] = 1
    for neig in graph[now]:
        if visited[neig] == 1:
            flag = 1
        if visited[neig] == 0:
            dfs(graph, visited, neig, ans)
    visited[now] = 2
    ans.append(now)


n, m = map(int, input().split())
graph = {}
visited = [0] * (n + 1)
ans = []
flag = 0

for i in range(1, n + 1):
    graph[i] = []

for i in range(m):
    lhs, rhs = map(int, input().split())
    graph[lhs] += [rhs]

for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(graph, visited, i, ans)
if flag == 1:
    print(-1)
else:
    for i in range(len(ans) - 1, -1, -1):
        print(ans[i], end=' ')