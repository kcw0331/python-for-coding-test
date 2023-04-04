# participant => 마라톤에 참여한 선수들의 이름
# 참가자 중에는 동명이인이 있을 수 있다.
# completion => 완주한 선수들의 이름이 담긴 배열
# return => 완주하지 못한 선수의이름
def solution(participant, completion):
    answer = ''
    par_dict = {} # 해시 문제라서 딕셔너리를 사용

    # 참가자별로 이름을 가지고 카운트를 실행
    for i in participant:
        if i in par_dict:
            par_dict[i] += 1
        else:
            par_dict[i] = 1
    # 출력하였을 때, mislav:2, stanko:1, ana:1이 됨
    # 완주한 배열을 가지고 완주한 사람이 있으면 -1해줌
    for j in completion:
        if j in par_dict:
            par_dict[j] -= 1
    # 출력하였을 때, mislav:1, stanko:0, ana:0이 됨
    for k in par_dict:
        if par_dict[k] == 1:
            answer += k
    # 이후 value의 값이 1인 것의 key값을 출력해준다.
    return answer