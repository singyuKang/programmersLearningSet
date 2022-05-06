from collections import deque

n, m , v = map(int, input().split())
graph = [[0]*(n+1) for k in range(n+1)]
visited_dfs = [0]*(n+1)

# print(graph)

for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')

    for i in range(n+1):
        if visited_dfs[i] == 0 and graph[i][v]:
            dfs(i)

visited_bfs = [0]*(n+1)

def bfs(v):
    visited_bfs[v] = 1
    que = deque()
    que.append(v)

    while que:
        node = que.popleft()
        print(node, end= ' ')
        for i in range(n+1):
            if visited_bfs[i] == 0 and graph[i][node]:
                que.append(i)
                visited_bfs[i] = 1
dfs(v)
print()
bfs(v)






