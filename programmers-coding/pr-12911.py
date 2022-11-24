# 프로그래머스 12911번: 다음 큰 숫자
def solution(n):
    n_new = n
    while True:
        n_new += 1 
        if n_new > n and (format(n, 'b').count("1") == format(n_new, 'b').count("1")):
            return n_new
            break