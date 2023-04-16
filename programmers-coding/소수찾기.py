from itertools import permutations
def primenumber(x):
    if x < 2:
        return False
    for i in range(2, x):	
    	if x % i == 0:		
            return False
    return True

def solution(numbers):
    answer = 0
    
    num = []
    for i in range(1, len(numbers)+1) :
        num.append(list(set(map(''.join, permutations(numbers, i)))))
    per = list(set(map(int, set(sum(num, [])))))
    
    for p in per :
        if primenumber(p) == True :
            answer += 1

    return answer

# ========================================================================
# 2023년 4월 16일 문제를 다시 풀어봄.
from itertools import permutations
def primenumber(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    result = []
    for number in range(1, len(numbers)+1):
        first = list(set(map(''.join, permutations(numbers, number))))
        result.append(first)
    unduplicated_numbers = list(set(map(int, sum(result, []))))
    
    for i in unduplicated_numbers:
        if primenumber(i) == True:
            answer += 1
    return answer