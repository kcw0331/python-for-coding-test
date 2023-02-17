# 백준 - 문자열 집합(14425번)
"""
문제
총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다. 

다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.

다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

출력
첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.
"""

"""
예제 입력 
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink

예제 출력
4
"""
n, m = map(int, input().split()) # n, m의 값을 받는다.
n_set = [] # 빈 리스트를 생성
for _ in range(n): # n개 만큼 for문을 돌린다.
  n_set.append(input()) # 얻어오는 값을 리스트에 추가
n_dict = {} # 값을 바로 찾아오기 위해 빈 딕셔너리 생성
for i in n_set: # 리스트를 for문을 돌며 딕셔너리 추가
    # value값은 1로 해준다.
  n_dict[i] = 1
cnt = 0 # 카운트를 하기 위해 0으로 초기화
for _ in range(m): # m개 만큼 for문을 돌린다.
  try: # try와 except를 사용해서 오류를 이용한다.
    n_dict[input()] # try에서 딕셔너리의 키값에 input을 하였을 때,
    # 값이 있으면 cnt에 1을 더하기
    cnt += 1
  except: # 값이 없다면 except문을 사용해서 0을 더하기
    cnt += 0
print(cnt) # 마지막에 카운트된 값을 출력해준다.