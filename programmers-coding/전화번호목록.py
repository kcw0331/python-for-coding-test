"""
전화번호부에 적힌 전화번호를 담긴 배열: phone_book
result: 어떤 번호가 다른 번호의 접두어인 경우가 있으면 => false 아니면 true
처음에 잘못 생각했던 부분은 맨 앞의 첫번째가 두번째 이후의 전화번호의 접두어가 되는지만 판단하였다.
하지만 다른 사람들의 풀이를 보았을 때, 어떤 번호가 다른 번호의 접두어가 된다고 판단하면 될 것 같다고 생각하였다.
이렇게 생각하고 풀어보니 정답이 되었다.
"""
def solution(phone_book):
    # 작은 것 부터 정렬
    phone_book.sort()
    # 앞, 뒤, 앞, 뒤해서 슬라이드를 사용해서 어떤 번호가 다른 번호의 접두어인지를 판단하였다.
    for i in range(1, len(phone_book)):
        secure = phone_book[i-1] # 처음에는 0, 1, 2로 해서 순서대로 바뀐다.
        secure_len = len(secure) # 길이를 사용해준다.
        if phone_book[i][:secure_len] == secure: # 슬라이드를 사용해서 접두어가 되는지를 판단해준다.
            return False
    return True