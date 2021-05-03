#https://www.acmicpc.net/problem/1389

# 1, 3 / 1, 4 / 2, 3 / 3, 4 / 4, 5
import sys
INF = sys.maxsize
n, m = map(int, input().split())
# 무한값으로 초기화
a = [[INF]*n for _ in range(n)]

# 간선 간의 weight 1로 초기화
for i in range(m):
    x, y = map(int, input().split())
    a[x-1][y-1] = 1
    a[y-1][x-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                a[i][j] = 0 # 자기자신한테가는건 0
            else:
                a[i][j] = min(a[i][j], a[i][k] + a[k][j])
ans = []
for i in a:
    ans.append(sum(i))  # 각 row 별 sum 값
for i in range(n):
    if ans[i] == min(ans):
        print(i+1) # idx 
        break