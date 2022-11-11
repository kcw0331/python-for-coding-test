# 뱍준 2292번: 벌집
# 첫번째 1과 마지막 7의 차 -> 6
# 7과 마지막 19의 차 -> 12
# 19와 37의 차 -> 18
N = int(input())

beehouse = 1
count = 1

while N > beehouse:
  beehouse += 6 * count 
  count += 1
print(count)