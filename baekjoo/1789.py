"""
백준(1789번) - 그리디(수들의 합)
문제
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
입력
첫째 줄에 자연수 S(1 <= S <= 4,294,967,295)가 주어진다.
출력
첫째 줄에 자연수 N의 최댓값을 출력한다.
"""
from time import time
import sys
input = sys.stdin.readline
start = time()
n = int(input())
n_sum = 0
result = 0
for i in range(1, n + 1):
  n_sum += i
  result += 1
  if n_sum > n:
    result -= 1
    break
end = time()
print(result, round(end - start, 3))
"""
예제 입력 1
200
예제 출력 1
19

예제 입력을 200을 주고 break를 했을 때, 시간을 재보면 2.432가 걸리게 된다.
그리고 예제 입력을 200을 주고 break를 하지 않았을 때, 시간을 재보면 38.512가 걸리게 된다.
if문에서 break를 왜? 걸었지 하고 시간을 재보니 break를 걸지 않으면 계속해서 for문을 돌게 되고, result -= 1을 하게 되서 시간이 증가하게 된다.
결론적으로 출력되는 결과는 같지만 break를 하지 않게 되면 시간이 많이 걸린다는 것을 알 수 있게 되었다.
"""
