# 백준(11659번) - 누적합(구간 합 구하기4)
import sys

def inp():
  return sys.stdin.readline()

n, m = map(int, inp().split())
n_list = list(map(int, inp().rstrip().split()))
pre = [0]
result = 0

for i in range(n):
  result += n_list[i]
  pre.append(result)

for i in range(m):
  a, b = map(int, inp().split())
  print(pre[b] - pre[a-1])