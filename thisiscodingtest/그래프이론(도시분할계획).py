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
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
print(result-cost)