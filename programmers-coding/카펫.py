# 2023년 4월 17일 
# 프로그래머스 - 고득점 kit - 완전탐색(카펫)
def solution(brown, yellow):
    answer = []
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_y = i
            yellow_x = int(yellow/i)
            if (yellow_x * 2) + (yellow_y * 2) + 4 == brown:
                answer.append(yellow_x + 2)
                answer.append(yellow_y + 2)
                # print(answer)
                return answer