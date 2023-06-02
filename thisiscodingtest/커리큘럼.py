# 입력 조건 - 위상 정렬을 사용한다.
# - 첫째 줄에 동빈이가 듣고자 하는 강의의 수 
from collections import deque
import copy

n = int(input()) # 노드의 개수 입력받기
indegree = [0] * (n + 1) # 모든 노드에 대한 진입차수는 0으로 초기화
graph = [[] for _ in range(n + 1)] # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
time = [0] * (n + 1) # 각 강의 시간을 0으로 초기화

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    # print(data[1:-1])
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree -= 1
            if indegree[i] == 0:
                q.append(i)
        for i in range(1, n + 1):
            print(result[i])
# topology_sort()