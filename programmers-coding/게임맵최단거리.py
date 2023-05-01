"""
maps: 게임 맵의 상태
return: 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값
만약, 상대 팀 진영에 도착할 수 없을 때는 -1을 return
"""
from collections import deque
def solution(maps):
    answer = 0
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            
            # 상하좌우 칸 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue
                if maps[nx][ny] == 0: continue
                
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
        return maps[len(maps)-1][len(maps[0])-1]    
    answer = bfs(0, 0)
    return -1 if answer == 1 else answer
    
    # return answer