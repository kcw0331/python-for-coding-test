# 백준 5597번: 과제 안 내신 분
N = 30
students = {s for s in range(1,N+1)}
student_N = []

for _ in range(N-2):
  student_N.append(int(input()))
student_N = set(student_N)
print(min(student_N ^ students))
print(max(student_N ^ students))