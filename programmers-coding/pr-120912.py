# 프로그래머스 120912번: 7의 개수
def solution(array):
    result = 0
    
    for i in array:
        if "7" in list(str(i)):
            result += list(str(i)).count("7")
    return result