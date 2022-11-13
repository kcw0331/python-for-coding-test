# 백준 1427번: 소트인사이드
n = str(input())
n_sort = []
for i in n:
  n_sort.append(int(i))
n_sort.sort(reverse = True)
result = ''
for i in n_sort:
  result += str(i)
print(result)