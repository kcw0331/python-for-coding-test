# 백준(2512번)-이진탐색(예산)
import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
m = int(input())
start, end = 0, max(array)

# start가 end보다 크다면 while문 종료
while start <= end:
  # 중간값을 정해준다.
  mid = (start + end) // 2
  # for문을 돌고난 후 최종값이 만들어진다.
  curr = 0
  for i in array:
    if i >= mid:
      curr += mid
    else:
      curr += i
  # for문을 돌고난 후 최종값을 m과 비교를 하면서
  # 값을 올릴지 내릴지 정한다.
  if curr <= m:
    start = mid + 1
  else:
    end = mid - 1
print(end)
