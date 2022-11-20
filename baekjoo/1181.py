# 백준 1181번: 단어 정렬
n = int(input())
word = []
for _ in range(n):
  word.append(str(input()))
set_word = list(set(word))

sort_word = []
for i in set_word:
  sort_word.append((len(i), i))
sort_word.sort()

for i, j in sort_word:
  print(j)