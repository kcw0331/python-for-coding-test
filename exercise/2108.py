# 백준 2108번: 통계학
import sys
from collections import Counter

N = int(sys.stdin.readline())
N_list = [int(sys.stdin.readline()) for _ in range(N)]
cent = int((len(N_list)//2))

mode = Counter(sorted(N_list)).most_common(2)

print(round(sum(N_list)/len(N_list)))
print(sorted(N_list)[cent])
print(mode[1][0] if len(mode) > 1 and mode[0][1] == mode[1][1] else mode[0][0])
print(max(N_list) - min(N_list))