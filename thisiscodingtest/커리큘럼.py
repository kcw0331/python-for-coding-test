# 입력 조건 - 위상 정렬을 사용한다.
# - 첫째 줄에 동빈이가 듣고자 하는 강의의 수 

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