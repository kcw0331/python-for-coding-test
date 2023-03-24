# 프로그래머스 코딩테스트 연습
# 정렬 - H-Index문제
# H-Index는 과학자의 생산성과 영향력을 나타내는 지표

def solution(citations):
    citations.sort(reverse=True)
    # enumerate를 사용해서 논문수와 인용 횟수가 같으면 출력
    # 아니면 논문수 보다 인용 횟수가 작아지는 지점인 것을 출력
    for i, j in enumerate(citations, start=1):
        if i == j:
            return i
        elif i > j:
            return i - 1
    return len(citations)
    # 만약에 [0,0,0,0]인 경우에 값이 안나올 수 있어서, 
    # return len(citations)을 써서 길이를 출력해준다
