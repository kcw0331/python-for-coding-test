# 6-2.py 파이썬 스와프(Swap) 소스코드
# 0 인덱스와 1 인덱스의 원소 교체하기
array = [3, 5]
array[0], array[1] = array[1], array[0]
# 파이썬에서는 바로 위의 코드를 사용해서 array의 위치를 변경해줄 수 있다.
print(array)