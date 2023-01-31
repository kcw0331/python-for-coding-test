# 숫자 카드2
n = int(input())
n_array = list(map(str, input().split()))

n_array_dict = {}
for c in n_array:
    if c not in n_array_dict:
        n_array_dict[c] = 1
    else:
        n_array_dict[c] += 1

m = int(input())
m_array = list(map(str, input().split()))

for i in m_array:
    if i in n_array_dict:
        print(n_array_dict[i], end=" ")
    else:
        print("0", end=" ")