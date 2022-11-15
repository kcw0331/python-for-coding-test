# 백준 11651번: 좌표 정렬하기2
import sys

n = int(sys.stdin.readline())
n_list = []
for _ in range(n):
  n_list.append(list(map(int, sys.stdin.readline().split())))
n_list.sort(key=lambda x: (x[1], x[0]))

for i in n_list:
  print(i[0], i[1])