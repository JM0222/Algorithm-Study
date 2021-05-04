#https://www.acmicpc.net/problem/1543

#Sol: b의 길이만큼 a를 자르면서 비교후 카운팅 해준다.
a = 'ababababa'
b = 'aba'
len_a = len(a)
len_b = len(b)
i = 0
answer = 0
while i <= len_a - len_b:
    if a[i:i+len_b] == b: # 같은경우 answer += 1 , 인덱스는 len_b만큼증가
        answer += 1
        i += len_b 
    else:
        i += 1
print(answer)
