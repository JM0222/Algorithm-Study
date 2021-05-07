#https://www.acmicpc.net/problem/2847
#check
n = int(input())
level = []
for i in range(n):
    level.append(int(input()))

max_level = level[-1]  # 가장뒤에있는값이 제일 커야한다(정렬이되야함)
cnt = 0
for i in range(len(level)-2,-1,-1): #뒤에서부터 순회
    if level[i] >= max_level:  # 정렬이 안되있는경우
        k = level[i] - max_level + 1  
        cnt += k  
        max_level = level[i] - k # +1해준만큼 뺴줘야 정렬
    else: # max값 갱신
        max_level = level[i]
print(cnt)