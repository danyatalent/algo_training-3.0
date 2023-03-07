
f = open('input.txt')


def DFS(graph_map, visited, ans):
  stack = [iter(range(len(graph_map), 0, -1))]
  while stack:
    try:
      child = next(stack[-1])
      if not visited[child]:
        visited[child] = True
        ans.append(child)
        stack.append(iter(graph_map[child]))
    except StopIteration:
      stack.pop()


def dfs(graph, visited, now, ans):
    visited[now] = True
    ans += [now]
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, ans)


n, m = map(int, f.readline().split())
graph = {}
ans = []
visited = [False] * (n + 1)

for i in range(1, n + 1):
    graph[i] = []

for i in range(m):
    lhs, rhs = map(int, f.readline().split())
    if rhs != lhs:
        graph[lhs].append(rhs)
        graph[rhs].append(lhs)

if m > 100000:
   DFS(graph, visited, ans)
else:
   dfs(graph, visited, 1, ans)
print(len(ans))
print(*sorted(ans))