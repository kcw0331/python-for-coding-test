# 백준(11399번) -ATM
import sys
def input():
  return sys.stdin.readline()
n = int(input())
time_list = list(map(int, input().rstrip().split()))
time_list.sort()
result = 0
for i in range(1, n + 1):
  result += sum(time_list[0:i])
print(result)