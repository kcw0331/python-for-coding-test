"""
그래프 이론
2. 팀 결성(서로소 집합 자료구조)
- 학생들에게 0 ~ N까지 번호 부여, 총 N + 1개의 팀 존재
- 선생님 => "팀 합치기", "같은 팀 여부 확인" 사용가능
- 특정 원소가 속한 집합 찾기
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

N, M = map(int, input().split())
parent = [0] * (N + 1)

for i in range(0, N + 1):
    parent[i] = i # 예) [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(M):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')

"""
result 
7 8
0 1 3
1 1 7
NO
0 7 6
1 7 1
NO
0 3 7
0 4 2
0 1 1
1 1 1
YES
"""