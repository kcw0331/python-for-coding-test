# 2019년 카카오 개발자 겨울 인턴십 (튜플)
import re
# 정규식을 사용함
# 길이가 작은 순으로 정렬 후
# 값이 있으면 -> append x, 값이 없으면 -> append o
def solution(s):
    s_list = []
    s = re.findall('\d+(?:\,\d+)*', s)
    s = sorted(s, key = len)
    for i in s:
        for j in i.split(','):
            j = int(j)
            if j not in s_list:
                s_list.append(j)
    return s_list