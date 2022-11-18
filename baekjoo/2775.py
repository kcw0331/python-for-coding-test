# 백준 2775번: 부녀회장이 될테야
t = int(input())  # Test case

for _ in range(t):
  k = int(input())  # 방
  n = int(input())  # 호
  people = [i for i in range(1, n+1)]  # 사람들 수만큼 리스트를 만듦
  for i in range(k):
    for j in range(1, n):
      people[j] += people[j - 1]  # 더해서 값이 순차적으로 증가함
  print(people[-1])  # 가장 마지막에 있는 값 출력