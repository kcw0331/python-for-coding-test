# 백준 - 재귀(좌표 압축)

"""
문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
"""

"""
입력

첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력

첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
"""
n = int(input()) # 첫째 줄에 N이 주어진다.
x = list(map(int, input().split())) # 공백으로 한칸씩 X들의 값이 주어진다.

x_set = set(x) # set을 사용해서 중복을 제거
x_set = sorted(list(x_set)) # set을 list로 변환후 오름차순으로 정렬
x_dir = dict()

for num, i in enumerate(x_set): # enumerate로 자리수와 값을 for문으로 돌림
  x_dir[i] = num # for문을 돌면서 딕셔너리에 집어넣어준다.
  # x_dir 출력 결과 : {-10: 0, -9: 1, 2: 2, 4: 3}

# 다시 for문을 돌면서 마지막 출력값 출력
for j in x:
  print(x_dir[j], end = " ") # 출력 결과 : 2 3 0 3 1