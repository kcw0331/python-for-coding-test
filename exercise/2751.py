# 백준 2751번: 수 정렬하기2
N = int(input())

N_list = [int(input()) for _ in range(N)]

for i in sorted(N_list):
  print(i)