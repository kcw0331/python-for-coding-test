# 6-7.py sorted 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# result = sorted(array)
# print(result)

# 6-8.py sort 소스 코드
# array.sort()
# print(array)

# 6-9.py 정렬 라이브러리에서 key를 활용한 소스코드
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)