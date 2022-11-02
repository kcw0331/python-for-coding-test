# 백준 2738번: 행렬 덧셈
N, M = map(int, input().split())
results = [[0] * M for _ in range(N)]

for i in range(N):
  A = list(map(int, input().split()))
  for j in range(M):
    results[i][j] += A[j]
    
for i in range(N):
  B = list(map(int, input().split()))
  for j in range(M):
    results[i][j] += B[j]

for result in results:
  print(*result)