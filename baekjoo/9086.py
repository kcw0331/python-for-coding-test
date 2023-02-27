# 백준(9086번) - 문자열
n = int(input())
result = []
for i in range(n):
  a = list(input())
  b = a[0] + a[-1]
  result.append(b)
for j in result:
  print(j)