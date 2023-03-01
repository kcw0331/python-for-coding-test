# 백준(1874번) - 스택(스택 수열)
import sys
n = int(sys.stdin.readline())
stack = []
result = []
flag = 0
cur = 1
for _ in range(n):
  num = int(sys.stdin.readline())
  while cur <= num:
    stack.append(cur)
    result.append("+")
    cur += 1
  if stack[-1] == num:
    stack.pop()
    result.append("-")
  else:
    print("NO")
    flag = 1
    break
if flag == 0:
  for i in result:
    print(i)
    