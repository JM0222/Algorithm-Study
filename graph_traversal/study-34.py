#https://www.acmicpc.net/problem/2178
#check
import queue
n, m = map(int,input().split())
map = [list(map(int,input())) for _ in range(n)]

q = queue.Queue()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
visit = [[0]*m for i in range(n)]

visit[0][0] = 1
q.put([0,0])

while not q.empty():
    x,y = q.get()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if nx < 0 or ny <0:
            continue
        if nx >= n or ny >= m:
            continue
        if map[nx][ny] == 0:
            continue
        if visit[nx][ny] !=0:
            continue
        visit[nx][ny] = visit[x][y] + 1
        q.put([nx,ny])
print(visit[n-1][m-1])