#https://www.acmicpc.net/problem/1012
from collections import deque
tc = int(input())
for i in range(tc):
    a, b, c = map(int,input().split()) ## a,b = 가로,세로 c = 배추개수
    board = [[0]*b for _ in range(a)]
    for i in range(c): # 맵 만들기
        cab_a, cab_b = map(int,input().split())
        board[cab_a][cab_b] = 1
    q = deque()
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    visit = [[0]*b for _ in range(a)]
    cnt = 0
    for i in range(a):
        for j in range(b):
            if board[i][j] == 1 and visit[i][j] == 0:
                q.append([i,j])
                visit[i][j] = 1
                cnt +=1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = dx[k] + x
                        ny = dy[k] + y
                        
                        if nx < 0 or ny < 0:
                            continue
                        if nx >= a or ny >= b:
                            continue
                        if visit[nx][ny] != 0:
                            continue
                        if board[nx][ny] == 0:
                            continue
                        visit[nx][ny] = 1
                        q.append([nx,ny])
    print(cnt)
