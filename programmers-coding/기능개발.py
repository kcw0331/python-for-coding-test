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
        # while progresses[number] <= 100:
        while progresses[number] < 100:
            progresses[number] += speeds[number]
            cnt += 1
        # results.append(cnt-1)
        results.append(cnt)
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

# 계속해서 시도를 해보았지만, 답을 찾을 수 없어서 chat GPT4에게 물어본 결과
# 1. 'while progresses[number] <= 100:' 부분에서 작업 진도가 정확히 100이 되는 경우에는 루프가 계속 실행된다고 한다.
# 그래서 조건을 'while progresses[number] < 100:'으로 변경해야 한다.
# 2. 'cnt-1' 부분에서 cnt값을 1 빼는 것은 불필요해 보인다. 그대로 cnt값을 사용하면 된다.