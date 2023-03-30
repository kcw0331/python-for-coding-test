import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

cnt = 0
visited = [False] * (n+1)

def dfs(v):
  global cnt
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(i)
      cnt += 1
dfs(1)
print(cnt)
