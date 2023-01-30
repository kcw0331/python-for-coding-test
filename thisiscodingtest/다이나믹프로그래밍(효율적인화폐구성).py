# 다이나믹프로그래밍 - 효율적인 화폐 구성
# 입력 조건
# 첫째 줄에 N, M이 주어진다. (1 <= N <= 100, 1 <= M <= 10,000)
# 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.
# 출력 조건 
# 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
# 불가능할 때는 -1을 출력한다.
"""
입력 예시 1
2 15 
2
3
출력 예시 1
5
"""
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])