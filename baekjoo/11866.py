from collections import deque
n, k = map(int, input().split())
q = deque()
result = []
for i in range(1, n + 1):
  q.append(i)

while q:
  for i in range(k-1):
    q.append(q.popleft()) 
  result.append(str(q.popleft()))
print("<", ", ".join(result), ">", sep = '')
