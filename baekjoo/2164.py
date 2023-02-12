# 백준 - 큐(카드2)
from collections import deque
n = int(input())
queue = deque()
for i in range(1, n + 1):
  queue.append(i)

# while문을 사용하여 1개가 남으면 스톱
while len(queue) > 1:
  # 두가지 절차를 따른다.
  # 첫번째, 왼쪽에서 하나를 꺼낸다.
  # 두번째, 왼쪽에서 하나를 또 꺼내서
  # 다시 집어넣어 준다.
  queue.popleft()
  queue.append(queue.popleft())
print(queue[0])