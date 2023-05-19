import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    result = (denom1 * numer2) + (denom2 * numer1)
    denom = denom1 * denom2
    gcd = math.gcd(denom, result)
    return [result // gcd, denom // gcd]