# 프로그래머스-완전탐색(전력망을 둘로 나누기)
from collections import deque
def bfs(graph, start, n):
    visited = [False] * (n+1)
    # 큐 구현을 위해 deque라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문처리 해준다
    visited[start] = True
    cnt = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt
                
def solution(n, wires):
    result = 0
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    result = n
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        result = min(abs(bfs(graph, a, n) - bfs(graph, b, n)), result)
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    return result