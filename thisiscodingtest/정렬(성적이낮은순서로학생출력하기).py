# 정렬 3. 성적이 낮은 순서로 학생 출력하기
# 입력 조건
# 첫 번째 줄에 학생의 수 N이 입력된다.(1 <= N <= 100,000)
# 두 번째 줄부터 N + 1번째 줄에는 학생의 이름을 나타내는 문자열 A
# 와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
# 문자열 A의 길이와 학생의 성적은 100이하의 자연수이다.
# 출력 조건
# 모든 학생의 이름을 성적이 낮은 순서대로 출력한다.
# 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.

# N을 입력받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []

for i in range(n):
    a, b = input().split()
    # a, b로 input 2개를 받아온다.
    array.append([a,b])
    # key를 사용해서 2번째 index를 기준으로 오름차순 정렬
array.sort(key=lambda x: x[1])

# 정렬이 수행된 결과를 출력
for i, _ in array:
    print(i, end=' ')