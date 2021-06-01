#https://www.acmicpc.net/problem/18405
#check
#(*)
from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
board = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    a = list(map(int,input().split()))
    board.append(a)
s, target_x, target_y = map(int,input().split())

#=====================================================

def infection():
    while q:
        virus, x, y, time = q.popleft() 
        if time == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0:
                continue
            if nx >= n or ny >= n:
                continue
            if board[nx][ny] != 0:
                continue
            board[nx][ny] = virus
            q.append([virus, nx, ny, time+1]) #time += 1

# 탐색하면서 q에 추가 할때 한번에 해줘야 시간초과가 안뜬다
q = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            q.append([board[i][j],i,j,0])
q.sort()  # 정렬시 제일 앞의 값 기준으로 sort 된다
q = deque(q)
infection()

print(board[target_x-1][target_y-1])