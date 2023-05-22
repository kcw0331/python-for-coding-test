from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
print(indegree)
print(graph)
# ex) indegree => [0, 0, 1, 1, 2, 1, 2, 1]
# ex) graph => [[], [2, 5], [3, 6], [4], [7], [6], [4], []]