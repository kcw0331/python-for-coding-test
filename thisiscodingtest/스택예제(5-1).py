stack = []
# append를 사용하여 왼쪽으로 쌓음
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
# pop을 사용하여 오른쪽부터 뺌
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # stack을 출력
print(stack[::-1]) # stack의 순서를 변경