"""
입력예시:
3 3
1 2
1 3
2 3
"""
# 특정 원소가 속한 잡합을 찾기
def find_parent(parent, x):
    # 루투 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
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

v, e = map(int, input().split()) # v: 노드의 개수, e: 간선
parent = [0] * (v + 1) # [0, 0, 0, 0]

for i in range(1, v + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b): # 에) 1 == 2가 같지 않아서 else 실행
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")

"""
예)
[0, 1, 1, 3]
[0, 1, 1, 1]
-> a = 2, b = 3을 실행할 때, 1 == 1이 같기 때문에 cycle = True가 되고 break가 된다.
"""