# 백준(10817번) - 구현(세 수)
"""
문제
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다.
출력
두 번째로 큰 정수를 출력한다.
"""
import sys
input = sys.stdin.readline()
# 입력을 리스트로 만듦
array = list(map(int, input.split()))
# list인 array를 sort를 사용해서 정렬
array.sort()
print(array[1])
