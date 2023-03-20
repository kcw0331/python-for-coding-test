# 백준(2751번) - 정렬(세수정렬)
import sys
input = sys.stdin.readline
n = list(map(int, input().split()))
n.sort()
for i in n:
  print(i, end=" ")
