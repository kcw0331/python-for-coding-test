#백준 11650번: 좌표 정렬하기
import sys
n = int(sys.stdin.readline().rstrip())
n_list = []
for _ in range(n):
  n_list.append(list(map(int, sys.stdin.readline().rstrip().split())))
n_list.sort()
for i, j in n_list:
  print(i, j)