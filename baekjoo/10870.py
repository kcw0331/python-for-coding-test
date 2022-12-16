# 백준 10870번: 피보나치 수 5 
n = int(input())
def fibo(n):
  if n <= 2 and n > 0:
    return 1
  elif n == 0:
    return 0
  return fibo(n-1) + fibo(n-2)

print(fibo(n))