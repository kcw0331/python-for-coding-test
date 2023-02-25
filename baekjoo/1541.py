# 백준(1541번) - 잃어버린 괄호
n = input().split('-')
result = []
for i in n:
  cnt = 0
  s = i.split('+')
  for j in s:
    cnt += int(j)
  result.append(cnt)
n = result[0]
for i in range(1, len(result)):
  n -= result[i]
print(n)