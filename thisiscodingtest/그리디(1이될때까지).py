# N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행함
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# 입력 조건: N, K
# 출력 조건: 수행해야 하는 횟수의 최솟값을 출력한다.

n, k = map(int, input().split())
count = 0
while n >= k:
    while n % k != 0:
        n -= 1
        count += 1
    n //= k
    count += 1
while n > 1:
    n -= 1
    count += 1
print(count)