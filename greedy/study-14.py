#https://www.acmicpc.net/problem/2847
n = int(input())
level = []
for i in range(n):
    level.append(int(input()))

max_level = level[-1]
cnt = 0
for i in range(len(level)-2,-1,-1):
    if level[i] >= max_level:
        k = level[i] - max_level + 1
        cnt += k
        max_level = level[i] - k
    else:
        max_level = level[i]
print(cnt)