# 탐색적알고리즘(음료수얼려먹기)
# N x M 크기의 얼음 틀
# 구멍이 뚫려 있는 부분 -> 0
# 칸막이가 존재하는 부분 -> 1
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것
# 4 5
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0
n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input().split())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if ice[x][y] == 0:
        # 해당 노드 방문 처리
        ice[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x -1, y)
        dfs(x, y -1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i  in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
print(result) # 정답 출력