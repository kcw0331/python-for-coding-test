# 백준 2750번: 수 정렬하기

N = int(input())
num_list = []
for _ in range(N):
  num_list.append(int(input()))
num_list1 = sorted(num_list)
for i in range(len(num_list)):
  print(num_list1[i])