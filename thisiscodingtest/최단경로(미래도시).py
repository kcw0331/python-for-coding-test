# 최단경로(미래도시)
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(n + 1):
    for b in range(n + 1):
        if a == b:
            graph[a][b] = 0

# 정확히 간선간의 소요시간은 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 소개팅녀의 회사를 지나서 마지막 도착하는 곳의 거리를 구한다.
distance = graph[1][k] + graph[k][x]

# Infinity보다 크다면 -1을 출력
if distance >= INF:
    print("-1")
else:
    print(distance) # 무한이 아니라면 거리를 출력한다.