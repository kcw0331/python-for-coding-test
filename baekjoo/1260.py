# 백준(1260번) - DFS와BFS
from collections import deque
def dfs(v):
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(i)
def bfs(v):
  queue = deque([v])
  visited[v] = True
  while queue:
    V = queue.popleft()
    print(V, end = ' ')
    for i in graph[V]:
       if not visited[i]:
         queue.append(i)
         visited[i] = True

n, m, v = map(int, input().split())

visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(v)
