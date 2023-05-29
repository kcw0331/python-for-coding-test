# 백준(1991번) - 트리(트리순회)
"""
입력
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

출력
ABDCEFG
DBAECFG
DBEGFCA
"""
n = int(input())
inputs = []
for _ in range(n):
  inputs.append(input().split())

class Node(): # 클래스 생성
  def __init__(self, item, left, right):
    # self를 사용해서 초기화
    self.item = item 
    self.left = left 
    self.right = right

def preorder(node): # 전위 순회
  print(node.item, end='') # 전위 순회라서 처음에 루트
  # if문을 두개 걸어줘서 재귀를 다하고 다은거를 재귀를 해준다.
  if node.left != '.':
    preorder(tree[node.left]) # 왼쪽이 있다면 왼쪽
  if node.right != '.': # 재귀가 이루어지게 된다.
    preorder(tree[node.right]) # 오른쪽이 있다면 오른쪽

def inorder(node): # 중위 순회
  if node.left != '.':
    inorder(tree[node.left])
  print(node.item, end = '')
  if node.right != '.':
    inorder(tree[node.right])

def postorder(node): # 후위 순회
  if node.left != '.':
    postorder(tree[node.left])
  if node.right != '.':
    postorder(tree[node.right])
  print(node.item, end = '')

tree = {}
for item, left, right in inputs: # inputs 리스트를 for문을 사용해서 하나씩 끄집어냄
  tree[item] = Node(item, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])


import sys

N = int(sys.stdin.readline().strip())
tree = {}

for i in range(N):
  root, left, right = sys.stdin.readline.strip()
  tree[root] = [left, right]

