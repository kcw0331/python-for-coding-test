# 프로그래머스 120886번: A로B만들기
def solution(before, after):
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0