# 개미 전사
# 입력 조건
# 첫째 줄에 식량창고의 개수 N이 주어진다.(3 <= N <= 100)
# 둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다.(0<=K<=1,000)
# 출력 조건
# 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오.
# 입력 예시
# 4
# 1 3 1 5
# 출력 예시
# 8
n = int(input()) # 정수 N을 입력
K = list(map(int, input().split())) # 모든 식량 정보 입력

d = [0] * 100 # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화

d[0] = K[0] # 
d[1] = max(K[0], K[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + K[i])
print(d[n - 1])