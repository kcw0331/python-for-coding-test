"""
도시분할계획 <= 클루스칼 알고리즘을 사용할 것 같다.
- 마을은 N개의 집
- 그 집들을 연결하는 M개의 길
- 마을 이장은 2개의 마을로 분할 하려한다
- 분리된 마을 안에 집들이 서로 연결되도록 분할해야한다.
- 분리된 마을의 임의의 두 집 사이에 경로가 항상 존재해야 한다.
- 마을에는 집이 하나 이상 있어야 한다.
- 분리된 두 마을 사이에 있는 길들은 필요가 없다.
"""
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

edges = []
result = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-cost)
# 가장 간단한 방법은 클루스칼 알고리즘으로 최소 신장 트리를 찾은 뒤에 최소 신장 트리를 구성하는 간선 중에서
# 가장 비용이 큰 간선을 제거하는 것이다. 그러면 최소 신장 트리가 2개의 부분 그래프로 나누어지며, 문제에서 요구하는 최적의 해를 만족한다.
