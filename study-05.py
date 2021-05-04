#https://www.acmicpc.net/problem/1931

# 10분
# 1 4  
# 3 5 
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14
n = int(input())
meeting = [] # (s, e)
for i in range(n):
    start, end = map(int,input().split())
    meeting.append((start, end))
# meeting.sort(key = lambda x: (x[1],x[0])) # 소팅
meeting.sort(key = lambda x: x[1],x[0])

# 끝나는 시간 기준으로 소팅해야 경우의 수가 많아진다
# 시작 시간 기준으로 소팅 한번더 해줘야 한다 
# (끝나는 시간 중복까지 고려)
answer = 0
i = 0
for start, end in meeting: # 시작시간 끝나는시간 비교해가며 갱신
    if start >= i:
        answer += 1
        i = end
print(answer)    