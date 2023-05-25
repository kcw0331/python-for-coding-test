from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1) # 모든 노드에 대한 진입차수를 [0, 0, 0, 0, 0, 0, 0, 0]로 0으로 초기화 한다
graph = [[] for i in range(v + 1)] # [[], [], [], [], [], [], [], []]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # [[], [2, 5], [3, 6], [4], [7], [6], [4], []]
    indegree[b] += 1 # [0, 0, 1, 1, 2, 1, 2, 1]
print(indegree)
print(graph)
# ex) indegree => [0, 0, 1, 1, 2, 1, 2, 1]
# ex) graph => [[], [2, 5], [3, 6], [4], [7], [6], [4], []]

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i) # 0이라면, 큐에 집어넣어 준다.

    # 큐 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0: 
                q.append(i) # 0이라면 큐에 넣어주고 아니라면 넘어간다.

    for i in result:
        print(i, end=' ')

topology_sort()