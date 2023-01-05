# 6-5.py 파이썬의 장점을 살린 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트의 길이가 1이하라면 반환
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗 <- 첫번째 원소
    tail = array[1:] # 피벗 이후의 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽

    # 분할 이후 피벗 왼쪽, 오른쪽 부분을 수행하고 붙여줌
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))