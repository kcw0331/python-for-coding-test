def solution(n):
    result = 0
    D = {}
    for i in range(1,11):
        N = 1
        for j in range(1,i+1):
            N *= j
        D[i] = N    # 1부터 10까지 팩토리얼 구한것을 딕셔너리에 추가
    for i in range(1,11):   
        if n >= D[i]:  # 최대의 i값을 찾아준다.
            print(i)
            result = i
    return result