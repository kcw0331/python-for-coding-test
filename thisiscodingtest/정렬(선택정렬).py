# 6-1.py 선택 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 0
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]: # 1,2,3,4,5,6,7,8
            min_index = j
            print(min_index)
    array[i], array[min_index] = array[min_index], array[i]
print(array)