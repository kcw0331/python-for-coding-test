# 백준(1920번)-정렬(수찾기)
import sys
input = sys.stdin.readline
n = int(input())
# list를 사용했다가 set으로 바꾸었다.
# list로 가져오게 되면 시간이 오래걸려서
n_arr = set(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
for i in m_arr:
  if i in n_arr:
    print(1)
  else:
    print(0)
