# 백준 - 4949번(균형잡힌 세상)
while True:
  n = input()
  stack = []

  if n == '.':
    break
    
  for i in n:
    if i == '(' or i == '[':
      stack.append(i)
    elif i == ')':
      if stack  and stack[-1] == '(':
        stack.pop()
      else:
        stack.append(i)
        break
    elif i == ']':
      if stack  and stack[-1] == '[':
        stack.pop()
      else:
        stack.append(i)
        break
  if not stack:
    print("yes")
  else:
    print("no")