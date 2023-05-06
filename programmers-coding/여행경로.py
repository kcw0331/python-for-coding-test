from collections import deque
def solution(tickets):
    answer = []
    # result = [False for _ in range(len(tickets))]
    queue = deque()
    # 출발 공항, 방문하는 공항 경로, 방문 경로를 저장(튜플을 사용)
    queue.append(("ICN",["ICN"],[]))
    
    while queue: # 큐에 값이 있을 때 까지만 while문 실행
        # 3개의 값을 왼쪽부터 추출
        airport, path, used = queue.popleft()
        # 전체 방문 경로와 티켓의 길이가 같다면, answer에 삽입
        if len(used) == len(tickets):
            answer.append(path) # answer에 path를 삽입
        # tickets을 for문을 사용
        for idx, ticket in enumerate(tickets):
            # ticket의 첫번째 변수와 airport가 같고 used에 없는 값이 라면 if을 실행
            if ticket[0] == airport and not idx in used:
                # 큐에 ticket의 두번째 값을 삽입
                queue.append((ticket[1], path + [ticket[1]], used + [idx]))
                # print(path)
    answer.sort() # 이후 answer를 오름차순으로 정렬
    return answer[0] # answer의 첫번째 변수를 출력