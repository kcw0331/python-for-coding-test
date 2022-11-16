# 그리디 알고리즘
# 백준 11047번: 동전 0
n, k = map(int, input().split())
count = 0

coin_type = []

for _ in range(n):
  N = int(input())
  if N <= k:
    coin_type.append(N)
    
coin_type.sort(reverse = True)

for coin in coin_type:
  count += k // coin
  k %= coin
print(count)