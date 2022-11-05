# 백준 - 10807번 개수 세기
# 리스트로 만들고
# count를 사용해서 찾으려는 값의 숫자를 세어준다.

int_number = int(input())
int_list = list(map(int, input().split()))
int_find = int(input())

print(int_list.count(int_find))