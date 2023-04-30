"""
컴퓨터의 개수: n
연결에 대한 정보가 담긴 2차원 배열: computers
네트워크의 개수: return
n: 3
computers: [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
2
"""
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            # DFS의 함수가 끝나게 되면 answer에 1을 더해준다.
            answer += 1
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        # if문이 만족이 된다면, DFS가 계속 이루어지게 된다
        # if문이 계속이루어 지게 된다면, 서로 연결되어 있다고 생각해도 될거 같다
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)