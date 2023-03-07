f = open('input.txt')

def dfs(graph, visited, now, comp, ans):
    stack = [now]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]: ans[comp] += [vertex]
        visited[vertex] = True

        for neig in graph[vertex]:
            if not visited[neig]:
                stack.append(neig)


n, m = map(int, f.readline().split())
graph = {}
visited = [False] * (n + 1)
ans = {}

for i in range(1, n + 1):
    graph[i] = []

for i in range(m):
    lhs, rhs = map(int, f.readline().split())
    graph[lhs] += [rhs]
    graph[rhs] += [lhs]

comp = 1
for i in range(1, n + 1):
    if not visited[i]:
        ans[comp] = []
        dfs(graph, visited, i, comp, ans)
        comp += 1
print(len(ans))
for comp in range(1, len(ans) + 1):
    print(len(ans[comp]))
    print(*ans[comp])