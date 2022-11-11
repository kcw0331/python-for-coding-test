# 백준 10989번: 수 정렬하기3
import sys
input = sys.stdin.readline
N = int(input())
N_list = [0]*10000

for i in range(N):
  a = int(input())
  N_list[a - 1] += 1

for i in range(10000):
  if N_list[i] != 0:
    for j in range(N_list[i]):
      print(i+1)