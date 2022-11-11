# 백준 - 25304번: 영수증 

price = int(input())
N = int(input())
a = []
for i in range(int(N)):
  a.append(list(map(int, input().split())))
  
total = 0

for j in a:
  total += (int(j[0]) * int(j[1]))

if price == total:
  print('Yes')
else:
  print('No')