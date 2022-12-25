# 5-3. 재귀 함수 예제
# def recursive_function():
#   print("재귀 함수를 호출합니다.")
#   return recursive_function()
# recursive_function()

# 5-4 재귀 함수 종료 예제
# def recursive_function(i):
#   # 100번째가 출력되면 종료하도록 종료 조건 추가
#   if i == 100:
#     return 
#   print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.")
#   recursive_function(i + 1)
#   print(i, "번째 재귀 함수를 종료합니다.")

# recursive_function(1)

# 5-5 2가지 방식으로 구현한 팩토리얼 예제
# 반복적으로 구현한 n!
def factorial_iterative(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n - 1)
print("반복적으로 구현", factorial_iterative(5))
print("재귀적으로 구현", factorial_recursive(5))