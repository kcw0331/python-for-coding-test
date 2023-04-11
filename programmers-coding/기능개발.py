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
            if result1[0] < a:
                result1.popleft()
                result1.append(a)
                answer.append(cnt1)
                cnt1 = 1
            elif result1[0] >= a:
                cnt1 += 1
    answer.append(cnt1)
    return answer

# 현재 11번 문제에서 막히는 현상이 생기고 있다. 
# 좋은 방법으로 문제를 푸는 방법도 있지만, 현재 이 방법을 사용해서 문제를 풀 수 없는지 계속해서 문제를 푸는 중이다.