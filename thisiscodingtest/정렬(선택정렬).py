# 6-1.py 선택 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 0 ~ 8까지 반복
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]: # 이부분이 n-1에서 가장작은 것을 찾아줌
            min_index = j # 가장 작은 수의 인덱스가 선택됨
    array[i], array[min_index] = array[min_index], array[i] # 스위치를 사용해서 작은 수와 맨 앞의 수를 바꾸어줌.
print(array)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <- 출력 결과 선택 정렬이 된 출력이 나오게 됨