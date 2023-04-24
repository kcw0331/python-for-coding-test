def solution(jobs):
    answer = 0
    # 정렬을 사용해서 두번째것을 기준으로 정렬을 해준다.
    jobs.sort(key = lambda x: x[1])
    result = [0]
    for a, b in jobs:
        result.append(int(result[0] + b)
    print(result)
    # return answer