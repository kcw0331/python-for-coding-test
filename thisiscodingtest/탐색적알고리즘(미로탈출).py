# 미로 탈출
# 괴물이 있는 부분은 0, 괴물이 없는 부분은 1
# 결과 -> 탈출하기 위해 움직여야 하는 최소 칸의 개수
# 첫줄 -> N, M
# 1 0 1 0 1 0
# 1 1 1 1 1 1
# 0 0 0 0 0 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
# x축과 y축의 이동할 방향을 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 맨 처음 시작 0, 0에서 부터 시작
    while queue:
        x, y = queue.popleft() # 큐에서 하나를 빼줌
        for i in range(len(dx)):
            nx = x + dx[i] # 왼쪽, 오른쪽으로 빼주고 더해줌
            ny = y + dy[i] # 위쪽, 아래쪽으로 빼주고 더해줌
            # 미로를 벗어날 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue 
            # 벽을 만날 경우도 무시
            elif graph[nx][ny] == 0:
                continue
            # 벽이 아닐 경우 이전의 값을 이후의 값에 더해줌
            # 이후의 값을 큐에 저장
            elif graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))