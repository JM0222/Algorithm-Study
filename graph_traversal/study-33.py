#https://www.acmicpc.net/problem/1926
#check
from collections import deque

n, m = map(int, input().split())

board = [list(map(int,input().split())) for _ in range(n)] # 맵

q = deque()
dx = [0,0,1,-1]
dy = [-1,1,0,0]
visit = [[0]*m for _ in range(n)] # 방문배열
cnt = 0
move_list = []
for i in range(n):
    for j in range(m):
        move = 1
        if board[i][j] == 1 and visit[i][j] == 0: # board 1, 방문하지않은경우
            q.append([i,j])
            cnt += 1
            visit[i][j] = 1 # 방문 check 
            while q:
                x, y = q.popleft()
                for k in range(4): 
                    nx = dx[k] + x
                    ny = dy[k] + y
                    
                    if nx < 0 or ny < 0:
                        continue
                    if nx >= n or ny >=m:
                        continue
                    if visit[nx][ny] != 0:
                        continue
                    if board[nx][ny] == 0:
                        continue
                    visit[nx][ny] = 1
                    move += 1  # 조건만족할때 move + 1
                    q.append([nx,ny])
            move_list.append(move) # 이동이 끝나면 append
if len(move_list) == 0:
    max_move_list = 0
else:
    max_move_list = max(move_list) # 넓이가 가장 큰값 
print(cnt) 
print(max_move_list)
            