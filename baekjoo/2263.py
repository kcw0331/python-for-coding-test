"""
백준(2263번) - (트리)트리의 순회
중위순회 -> 왼쪽, 루트, 오른쪽
후위순회 -> 왼쪽, 오른쪽, 루트
전위순회 -> 루트, 왼쪽, 오른쪽
코드를 만드는게 아직 잘 이해가 안된다.
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
inorder  = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodeNum = [0] * (n + 1)
for i in range(n):
  nodeNum[inorder[i]] = i

def preorder(istart, iend, pstart, pend):
  if (istart > iend) or (pstart > pend):
    return
  parent = postorder[pend]
  print(parent, end = ' ')

  left = nodeNum[parent] - istart
  right = iend - nodeNum[parent]

  preorder(istart, istart+left-1, pstart, pstart+left-1)
  preorder(iend-right+1, iend, pend-right, pend-1)
preorder(0, n-1, 0, n-1)
  
