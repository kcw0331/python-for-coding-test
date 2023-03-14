# 백준(2440번) - 구현(별 찍기-3)  
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n, 0, -1):
  print(i * "*")
