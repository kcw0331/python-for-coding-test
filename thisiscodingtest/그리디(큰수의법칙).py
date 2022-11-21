# 이것이 코딩테스트이다. -나동빈-
# 그리디 알고리즘 
# 실전문제 <큰 수의 법칙>
# 입력 조건 #
# 첫째 줄에는 N, M, K의 자연수
# 둘째 줄에는 N개의 자연수
# 5 8 3
# 2 4 5 4 6

# 출력 조건 #
# 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.
# 46

n, m ,k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
first = array[-1]
second = array[-2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1
print(result)