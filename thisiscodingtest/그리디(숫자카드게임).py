# 입력조건 
# 행의 개수 -> N, 열의 개수 -> M
# 출력 조건
# 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

# 입력예시
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

#출력 예시
3
n, m = map(int, input().split())
cards = []
for _ in range(n):
    cards.append(list(map(int, input().split())))
card_coise = []
for card in cards:
    card_coise.append(min(card))
print(max(card_coise))

#-------------------------------------------------------
# 3-3.py min()함수를 이용하는 담안 예시
# N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())
# result = 0
# 한 줄씩 입력받아 확인
# for i in range(n):
#   data = list(map(int, input(),split()))
#   # 현재 줄에서 '가장 작은 수' 찾기
#   min_value = min(data)
#   # '가장 작은 수'들 중에서 가장 큰 수 찾기
#   result = max(result, min_value)
# print(result) # 최종 답안 출력

#--------------------------------------------------------
# 3-4.py 2중 반복문 구조를 이용하는 답안 예시
# N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())
# result = 0
# 한 줄씩 입력받아 확인
# for i in range(n):
#   data = list(map(int, input(),split()))
#   # 현재 줄에서 '가장 작은 수' 찾기
#   min_value = 10001
#   for a in data:
#       min_value = min(min_value, a)
#   # '가장 작은 수'들 중에서 가장 큰 수 찾기
#   result = max(result, min_value)
# print(result) # 최종 답안 출력

