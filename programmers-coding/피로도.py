# 프로그래머스 - 완전탐색(피로도)
# 순열을 사용해서 던전 순서를 모두 만들어 주었다.
# 이후 만들어진 던전 순서를 사용하고 for문을 사용해서 result의 결과가
# 가장 많은 것으로 값을 바꾸어 주는 방식을 사용하였다.
from itertools import permutations
def solution(k, dungeons):
    answer = 0
    a = []
    for i in range(len(dungeons)):
        a.append(i)
    permute = permutations(a,len(dungeons))
    
    for j in permute:
        k_number = k
        result = 0
        for K in j:
            if dungeons[K][0] <= k_number:
                k_number -= dungeons[K][1]
                result += 1
            else:
                continue
        if result >= answer:
            answer = result
    return answer