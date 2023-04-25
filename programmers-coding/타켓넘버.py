# 프로그래머스 - BFS/DFS(타겟넘버)
from itertools import product
def solution(numbers, target):
    number = [(x, -x) for x in numbers]
    # product를 사용해서 데카르트 곱을 사용한다.
    number_list = list(map(sum, product(*number)))
    # print(number_list)
    return number_list.count(target)