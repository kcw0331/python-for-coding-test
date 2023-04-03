# 프로그래머스 해시 - 포켓몬
"""
제한 사항
- nums는 포켓몬의 종류 번호가 담긴 1차원 배열입니다.
- nums의 길이(N)는 1 이상 10,000이하의 자연수이며, 항상 짝수로 주어집니다.
- 포켓몬의 종류 번호는 1 이상 200,000이하의 자연수로 나타냅니다.
- 가장 많은 종류의 포켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 포켓몬 종류 개수의 최댓값 하나만 return하면 됩니다.
"""
def solution(nums):
    # 뽑을 수 있는 포켓몬의 개수를 구한다.
    sel = len(nums) // 2
    # set을 사용해서 중복되는 값을 제거
    nums = set(nums)
    # if문을 사용해서 같다면, len(nums)의 길이 출력
    if len(nums) == sel:
        return len(nums)
    # len(nums)가 selqhek 초과한다면, sel의 길이 출력
    elif len(nums) > sel:
        return sel
    # len(nums)가 sel보다 미만이라면, len(nums)의 길이 출력
    elif len(nums) < sel:
        return len(nums)