# n = int(input())
# first = 5
# second = 3
# result = 0
# while True:
#   if n % first == 0:
#     print(n // first)
#     break
#   elif n % second == 0:
#     print(n // second)
#     break
#   else:
#     n -= 3
#     result += 1
#     result += (n//first)
#     n = (n%first)
#     if n == 0:
#       print(result)
#       break
#     else:
#       result += (n//second)
#       n = (n%second)
#       if n != 0:
#         print(-1)
#         break
#       else:
#         print(result)
#         break
# 백준 2839번: 설탕 배달
n = int(input())

result = 0
while n >= 0:
  if n % 5 == 0:
    result += (n // 5)
    print(result)
    break
  n -= 3
  result += 1
else:
  print(-1)