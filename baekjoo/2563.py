# 백준 - 색종이(2563번)
n = int(input())
array = [[0] * 101 for i in range(101)]

for _ in range(n):
  a, b = map(int, input().split())
  for i in range(10):
    for j in range(10):
      array[a+i][b+j] = 1

result = 0
for i in array:
  result += sum(i)
print(result)