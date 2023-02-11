# 백준 - 9012번 괄호

n = int(input()) # 숫자 입력

for _ in range(n): # 입력한 숫자만큼 range를 돌려준다.
  stack = [] # 데이터를 집어넣어준 stack을 만들어준다.
  vpss = input() # 예를 들어, (())()가 들어가게 된다.
  for vps in vpss: # (())()가 for문을 사용해서 한개씩 들어가게 된다.
    if vps == '(': # 만약에 (가 나오게 되면 append
      stack.append(vps)
    elif vps == ')': # 만약에 )가 나오게 되면 조건문을 사용해서 
      if stack: # stack이 비어있지않으면 pop, 비어있다면 NO이 출력되고 break를 걸어준다.
        stack.pop()
      else:
        print("NO")
        break
  else: # break가 되지 않고 진행 되었다면
    if not stack: # stack이 비어 있다면 YES출력
      print("YES")
    else: # stack이 비어있지 않다면 NO출력
      print("NO")