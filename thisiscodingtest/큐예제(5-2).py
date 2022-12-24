from collections import deque

# 큐 구현을 위해 deque를 적용
queue = deque()
# append를 사용하여 오른쪽에서 추가
queue.append(5) 
queue.append(2)
queue.append(3)
queue.append(7)
# popleft를 사용하여 왼쪽부터 제거
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
# 출력
print(queue)
# reverse를 사용하여 방향변환
queue.reverse()
print(queue)