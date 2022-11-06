# codeup - 1805 : 입체기동장치 생산공장

n = input()  # 입체기동장치의 갯수 -> n
numbre = []  # 입체기동장치의 식별번호 a와 가스 보유량 b

for _ in range(int(n)): # n개의 갯수 만큼 for문을 돌려준다.
  numbre.append(list(map(int, input().split()))) # 식별번호와 가스 보유량을 numbre에 추가시킨다.

numbre.sort() # 리스트 첫번째꺼를 기준으로 오름차순 정렬

for i in numbre:
  print(*i) # 오름차순 정렬된거를 출력해준다.