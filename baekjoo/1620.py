from sys import stdin

def input():
    return stdin.readline().rstrip()
n, m = map(int, input().split())
dict_id = {}
dict_name = {}
for i in range(1, n+1):
  pokemon = input()
  dict_id[i] = pokemon
  dict_name[pokemon] = i
  
for _ in range(1, m+1):
  x = input()
  if x.isdigit():
    print(dict_id[int(x)])
  else:
    print(dict_name[x])
  