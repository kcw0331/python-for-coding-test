# BFS로 문제를 풀어보았다.
# 요즘은 DFS/BFS 문제가 나오면 BFS로 문제를 푸는게 더 편하고 쉽게 느껴진다.

from collections import deque
def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin, 0)) # 우선, 처음 큐에 시작단어와 깊이를 넣어준다.
    n = [False for _ in range(len(words))]
    
    while queue:
        x, y = queue.popleft()
        if x == target:
            answer = y
            break   
        for i in range(len(words)):
            if not n[i]:
                temp_n = 0
                for j in range(len(x)):
                    if x[j] != words[i][j]: # 단어가 1글자만 다를때, 큐에 넣어서 넣이 우선 탐색을 실시한다.
                        temp_n += 1
                if temp_n == 1:
                    queue.append((words[i], y + 1))
                    n[i] = 1
    return answer