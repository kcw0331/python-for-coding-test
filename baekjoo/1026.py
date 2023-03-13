# 백준(1026번)-정렬(보물)

import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True) # 큰 수대로 정렬을 해준다
b = list(map(int, input().split()))
b.sort() # 작은 수대로 정렬을 해준다
result = 0
for i in range(n): # n의 순서대로 곱하고 더해준다
  result += (a[i] * b[i])
print(result)

