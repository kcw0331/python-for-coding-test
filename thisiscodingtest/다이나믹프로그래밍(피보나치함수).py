"""
# 피보나치 함수
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
print(fibo(4))
"""

"""
# 호출되는 함수 확인 -> Top-down
d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x - 1) + pibo(x - 2)
    print(d)
    return d[x]
pibo(6)
"""

# 피보나치 수열 소스코드(반복적) -> bottom-up 
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1이다.
d[1] = 1
d[2] = 1

for i in range(3, 100):
    d[i] = d[i - 2] + d[i - 1]

print(d[4])