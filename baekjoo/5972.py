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
# 다익스트라 알고리즘
import heapq # 힙을 사용해준다.
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = [] # 빈 리스트를 만들어 준다.
  heapq.heappush(q, (0, start)) # 튜플을 사용해서 (거리, 노드)의 형태로 만든다.
  # 시작 노드의 거리는 0으로 초기화를 해준다. 
  dis[start] = 0 
  while q:
    d, now = heapq.heappop(q) # q에서 데이터를 꺼낸다
    if dis[now] < d: # 해당 노드의 거리(dis)가 현재 거리(d)보다 작으면 무시한다
      continue
    for v, w in graph[now]: # 처리되지 않은 노드들 중에서 해당 노드와 연결된 노드들(v)을 차례로 방문한다
      cost = d + w # 현재거리(d)와 해당 노드 사이의 거리(w)를 더한 값(cost)이 v의 현재 거리 (dis[v])보다 작으면, dis[v]를 갱신하고 우선순위 큐에(cos, v)의 형태로 데이터를 넣는다.
      if cost < dis[v]:
        dis[v] = cost
        heapq.heappush(q, (cost, v))
N, M = map(int, input().split())
# graph리스트에는 인덱스가 노드 번호인 리스트가 N + 1개 만들어지며, 각각의 리스트는 (연결된 노드, 거리)의 형태로 저장된다.
graph = [[] for _ in range(N+1)]
dis = [INF] * (N+1)
for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
dijkstra(1)
print(dis[N])
