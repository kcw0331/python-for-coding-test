n = int(input())
a = list(map(str, input().split()))
start_ = [1,1]

for i in a:
    if i == 'R':
        start_[1] += 1
        if start_[1] == n+1:
            start_[1] -= 1
    elif i == 'L':
        start_[1] -= 1
        if start_[1] == 0:
            start_[1] += 1
    elif i == 'U':
        start_[0] -= 1
        if start_[0] == 0:
            start_[0] += 1
    elif i == 'D':
        start_[0] += 1
        if start_[0] == n+1:
            start_[0] -= 1
print(start_[0], start_[1])