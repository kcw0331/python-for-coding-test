def solution(answers):
    answer = []
    
    first_cnt = 0
    second_cnt = 0
    third_cnt = 0
    
    first = [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000
    for i in range(len(answers)):
        if answers[i] == first[i]:
            first_cnt += 1
        if answers[i] == second[i]:
            second_cnt += 1
        if answers[i] == third[i]:
            third_cnt += 1
    if first_cnt > second_cnt and first_cnt > third_cnt:
        answer.append(1)
    elif second_cnt > first_cnt and second_cnt > third_cnt:
        answer.append(2)
    elif third_cnt > first_cnt and third_cnt > second_cnt:
        answer.append(3)
    elif first_cnt == second_cnt and first_cnt > third_cnt:
        answer.append(1)
        answer.append(2)
    elif first_cnt > second_cnt and first_cnt == third_cnt:
        answer.append(1)
        answer.append(3)
    elif first_cnt > second_cnt and second_cnt == third_cnt:
        answer.append(2)
        answer.append(3)
    elif first_cnt < second_cnt and second_cnt == third_cnt:
        answer.append(2)
        answer.append(3)
    elif third_cnt == first_cnt and third_cnt == second_cnt and second_cnt == first_cnt:
        answer.append(1)
        answer.append(2)
        answer.append(3)
    return answer