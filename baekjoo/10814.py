# 백준 10814번: 나이순 정렬
n = int(input())
member = []
for _ in range(n):
  age, name = input().split()
  member.append([int(age), name])
member.sort(key = lambda x : x[0])
for i in member:
  print(i[0], i[1])