#https://www.acmicpc.net/problem/1449

# 40분

# 입력받기
n, l = map(int,input().split())
hole = list(map(int,input().split()))
hole.sort() # 정렬

s = hole[0] - 0.5 + l  # 하나 테이프 붙어있다고 가정한후 
answer = 1             # 이 테이프가 커버가능한 길이 

for i in range(1, n): 
    if s < hole[i] + 0.5: # 커버불가능한 테이프범위내에 구멍이있으면 
        s = hole[i] - 0.5 + l # 새로운테이프를 붙이고 카운팅후, 새로운 범위 갱신
        answer += 1
    else:
        i = i+1
print(answer)



    