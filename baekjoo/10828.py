# 백준 - 스택(10828번)
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
"""
예제 입력1
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top

예제 출력1
2
2
0
2
1
-1
0
1
-1
0
3
"""
n = int(input())
result = []
array_list = []
for i in range(n):
  array = list(map(str, input().split()))
  if len(array) == 2 and array[0] == "push":
    array_list.append(array[1])
  elif array[0] == 'top':
    if len(array_list) != 0:
      result.append(array_list[-1])
    else:
      result.append(-1)
  elif array[0] == 'size':
    result.append(len(array_list))
  elif array[0] == 'empty':
    if len(array_list) == 0:
      result.append(1)
    else:
      result.append(0)
  elif array[0] == 'pop':
    if len(array_list) != 0:
      result.append(array_list.pop())
    else:
      result.append(-1)

for j in result:
  print(j)