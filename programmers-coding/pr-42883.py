# 프로그래머스 42883번: 큰 수 만들기
def solution(number, k):
    result = []

    for i in number:
        while k > 0 and result and result[-1] < i:
            result.pop()
            k -= 1
        result.append(i)
    return ''.join(result[:len(result) - k])