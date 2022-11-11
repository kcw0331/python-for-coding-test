# 백준 1316번: 그룹 단어 체커
N = int(input())
count = N

for _ in range(N):
  word = input()
  for i in range(len(word)-1):
    if word[i] == word[i+1]:
      pass # 위의 조건이 성립되면 아무것도 하지 않음.
    elif word[i] in word[i+1:]:
      count -= 1
      break # 위 조건이 성립되면 반복문을 끝냄.
print(count)
      