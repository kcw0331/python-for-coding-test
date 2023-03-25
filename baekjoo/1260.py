# 백준(1260번) - DFS와BFS
def dfs(v):
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(i)
      
n, m, v = map(int, input().split())

visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(v)
