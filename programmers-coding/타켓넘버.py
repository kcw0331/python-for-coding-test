# 프로그래머스 - BFS/DFS(타겟넘버)
from itertools import product
def solution(numbers, target):
    number = [(x, -x) for x in numbers]
    # product를 사용해서 데카르트 곱을 사용한다.
    number_list = list(map(sum, product(*number)))
    # print(number_list)
    return number_list.count(target)

# dfs 방식으로 문제를 푸는 방식이다.(다른 사람이 푼거를 dfs를 공부하기 위해 적어보았다.)
def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result+numbers[idx])
    dfs(0,0)
    return answer