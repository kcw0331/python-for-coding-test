# 프로그래머스 120887번: k의 개수
def solution(i, j, k):
    cnt = 0
    
    for l in range(i, j+1):
        string = str(l)
        string_list = list(string)
        if str(k) in string_list:
            cnt += string_list.count(str(k))
    return cnt