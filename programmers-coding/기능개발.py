"""
progresses: 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
speeds: 각 작업의 개발 속도가 적힌 정수 배열
answer: 각 배포마다 몇 개의 기능이 배포되는지
"""
from collections import deque
def solution(progresses, speeds):
    answer = []
    results = deque()
    for number in range(len(progresses)):
        cnt = 0
        while progresses[number] <= 100:
            progresses[number] += speeds[number]
            cnt += 1
        results.append(cnt-1)
    result1 = deque()
    cnt1 = 1
    while results:
        a = results.popleft()
        if len(result1) == 0:
            result1.append(a)
        else:
            if result1[0] <= a:
                result1.popleft()
                result1.append(a)
                answer.append(cnt1)
                cnt1 = 1
            elif result1[0] >= a:
                cnt1 += 1
    answer.append(cnt1)
    return answer