"""
백준(5972번) - 다익스트라(택배배송)
농부 현서, N개의 헛간과 소들의 길인 M개의 양방향 길이 그려져 있고, 각각의 길은 C_i마리의 소가 있다.
소들의 길은 두 개의 떨어진 헛간인 A_i와 B_i에 있다.
입력
첫째 줄에 N과 M이 공백을 사이에 두고 주어진다.
둘째 줄부터 M+1번째 줄까지 세 개의 정수 A_i, B_i, C_i가 주어진다.
출력
첫째 줄에 농부 현서가 가져가야 될 최소 여물을 출력하라.
"""
# 다른 분꺼를 보고 적어 보긴 하였으나 다익스트라 코드 만드는 것을 다시 내가 작성해보아야 할 것 같다.
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  dis[start] = 0
  while q:
    d, now = heapq.heappop(q)
    if dis[now] < d:
      continue
    for v, w in graph[now]:
      cost = d + w
      if cost < dis[v]:
        dis[v] = cost
        heapq.heappush(q, (cost, v))
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dis = [INF] * (N+1)
for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
dijkstra(1)
print(dis[N])
