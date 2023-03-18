# 백준(11721번) - 문자열(열개씩끊어출력하기)
# 슬라이싱을 사용하여 문제를 풀었다.
import sys
input = sys.stdin.readline
array = str(input().rstrip())

for i in range(0, len(array), 10):
  print(array[i:i + 10])
