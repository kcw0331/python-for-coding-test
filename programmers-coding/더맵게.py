"""
프로그래머스 - 힙(더맵게)
제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
"""
# heapq를 사용하여 문제를 해결함.
import heapq
def solution(scoville, K):
    answer = 0
    # 빈 리스트 생성
    heap = []
    for i in scoville:
        # for문을 사용하여 heap에 push
        heapq.heappush(heap, i)
    # 최소 횟수를 구해준다.
    cnt = 0
    # while문을 사용하여 스코빌 지수 K보다 크면 종료
    while heap[0] < K:
        # 만약 heap의 길이가 1개라면 -1을 리턴
        if len(heap) == 1:
            return -1
        # heappop을 사용하여 값이 작은 것을 끄집어냄
        # a: 첫번째 작은 것, b: 두번째로 큰 것
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        # 계산한 스코빌 지수를 c 변수로 입력
        c = a + (b * 2)
        # 한번 실행 될 때, +1을 더해준다.
        cnt += 1
        # 계산된 c를 heappush을 사용하여 heap에 넣어준다.
        heapq.heappush(heap, c)
    # 계산된 만들기 위해 섞어야 하는 최소 횟수를 cnt로 리턴
    return cnt