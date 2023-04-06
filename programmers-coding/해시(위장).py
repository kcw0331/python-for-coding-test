# 프로그래머스 해시 - 위장
"""
INPUT
스파이가 가진 의상들이 담긴 2차원 배열 clothes
OUTPUT
서로 다른 옷의 조합의 수
"""
def solution(clothes):
    _dict = {}
    result = 1
    for i, j in clothes:
        if j in _dict:
            _dict[j].append(i)
        else:
            _dict[j] = [i]
    for i in _dict.keys():
        result = result * (len(_dict[i]) + 1)
    return result - 1