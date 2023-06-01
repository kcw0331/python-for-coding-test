# 입력 조건 - 위상 정렬을 사용한다.
# - 첫째 줄에 동빈이가 듣고자 하는 강의의 수 
from collections import deque
import copy

n = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
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
topology_sort()