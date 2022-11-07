# 백준 25305번: 커트라인
# 첫째 줄 -> 응시자의 수 N, 상을 받는 사람의 수 -> K
# 둘째 줄 -> 각 학생의 점수 x
N, K= map(int, input().split())
x = list(map(int, input().split()))
x.sort(reverse = True)
print(x[K-1])