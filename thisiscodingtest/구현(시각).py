# N시에 대한 값을 받는다.
# N시를 기준으로 분과 초를 for문을 돌린다.
# 돌려서 3이 하나라도 포함되면 + 1 count해준다.
# 결과를 출력해준다.
n = int(input())
count = 0
for i in range(n+1): # 3이 들어갔는지 세기 위해서 str로 변환
    i = str(i)
    for j in range(60):
        j = str(j)
        for k in range(60):
            k = str(k)
            result = i+j+k # str로 만들고 count를 이용해서 3을 세어줌
            if result.count('3') >= 1: # 3을 세어서 1이상이면 count에 1을 추가
                count += 1
print(count) # 다 세어준 count 값을 출력