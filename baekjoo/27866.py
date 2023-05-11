# 문자와 문자열
"""
단어 $S$와 정수 $i$가 주어졌을 때, $S$의 $i$번째 글자를 출력하는 프로그램을 작성하시오..
"""
import sys
word = sys.stdin.readline()
number = sys.stdin.readline()
print(word[int(number)-1])