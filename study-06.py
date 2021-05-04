# https://www.acmicpc.net/problem/5525 //
# https://velog.io/@woga1999/BOJ-5525%EB%B2%88-IOIOI-Python
# TC

# 2 ioioi
# 13
# OOIOIOIOIIOII
# 시간 40분이상 구글링참조
n = int(input()) # n의값에따라 패턴의길이가 다르다
m = int(input())
s = input()

answer = 0
pattern = 0  
i = 1
while i < m-1:
    if s[i-1] == "I" and s[i] == "O" and s[i+1] == 'I':
        pattern += 1
        if pattern == n: 
            pattern -= 1
            answer += 1
        i += 1
    else:
        pattern = 0
    i += 1 #  idx 값 증가하면서 탐색
print(answer)