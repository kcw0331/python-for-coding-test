# 백준 2587번: 대표값2
num_list = []
for _ in range(5):
  num_list.append(int(input()))
num_list1 = sorted(num_list)

print(int(sum(num_list1)/len(num_list1)))
print(num_list1[2])
