# 부품찾기
""" 
# 내가 문제 풀어본 방식
import sys
n = int(input())
array = list(sys.stdin.readline().rstrip().split()) # 값을 읽어오고 리스트로 바꾸어줌
array.sort() # 리스트를 sort 메서드를 사용해서 오름차순 정렬
m = int(input()) 
array_find = list(sys.stdin.readline().rstrip().split())
array_find.sort()
result = [] # 마지막 결과 값을 집어넣어줌
# 찾으려는 부품을 for문을 사용해서 있으면 yes, 없으면 no로 해서 result에 append
for i in array_find:
    if i in array:
        result.append("yes")
    else:
        result.append("no")
# 리스트로 되어있는 result를 for문을 통해 출력을 해줌
for j in result:
    print(j, end=" ")
 """

# 책에 있는 방법을 사용하여 문제풀이
# 방법 1) 답안 예시(이진탐색)
# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid 
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번로를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M(손님이 확인 요청한 부품 개수) 입력
m = list(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n - 1)
    print(result)
    if result != None:
        print('yes', end=" ")
    else:
        print('no', end=" ")