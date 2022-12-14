# 백준 - 듣보잡 1764번
# 알고리즘 분류: 자료구조, 문자열, 정렬, 해시를 사용한 집합과 맵
"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
"""
n, m = input().split()
n_list = [input() for _ in range(int(n))]
n_list = set(n_list)
m_list = [input() for _ in range(int(m))]
m_list = set(m_list)

result = sorted(list(n_list & m_list))
print(len(result))

for i in result:
  print(i)