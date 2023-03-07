def dfs(graph, visited, now, prev):
    global start, end
    visited[now] = 1
    for neig in graph[now]:
        if visited[neig] == 1 and prev[now] != neig:
            end = now
            start = neig
            return True
        if visited[neig] == 0:
            prev[neig] = now
            if dfs(graph, visited, neig, prev): 
                return True
    visited[now] = 2
    return False


n = int(input())
gr = {}
visited = [0] * (n + 1)
start, end = -1, -1
prev = [0] * (n + 1)
ans = []

for i in range(1, n + 1):
    gr[i] = []

for i in range(1, n + 1):
    s = input().split()
    for j in range(1, n + 1):
        if int(s[j - 1]) == 1:
            gr[i] += [j]
for i in range(1, n + 1):
    if visited[i] == 0: 
        if dfs(gr, visited, i, prev):
            break
if start == -1:
    print('NO')
else:
    v = end
    while v != start:
        ans.append(v)
        v = prev[v]
    ans.append(start)
    print('YES')
    print(len(ans))
    print(*ans)


