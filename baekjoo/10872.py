# 백준 10872번: 팩토리얼
# 0보다 크거나 같은 정수 N이 주어진다.
n = int(input())
def fibo(n):
  if (n > 1):
    return n * fibo(n - 1)
  else:
    return 1

print(fibo(n))