#https://www.acmicpc.net/problem/16918
#check
#https://par3k.tistory.com/194
from collections import deque
a, b, c = map(int, input().split())
board = [list(input()) for _ in range(a)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def find():
    for i in range(a):
        for j in range(b):
            if board[i][j] == 'O':
                q.append([i,j])

def bombSet():
    for i in range(a):
        for j in range(b):
            if board[i][j] !='O':
                board[i][j] = 'O'

def bomb():
    while q:
        x, y = q.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0:
                continue
            if nx >= a or ny >= b:
                continue
            if board[nx][ny] == 'O':
                board[nx][ny] = '.'
c -= 1 # 1초 지난거 세팅
while c:
    q = deque()
    find()
    bombSet()
    c -= 1
    if c == 0:
        break
    bomb()
    c -= 1

for i in range(a):
    for j in range(b):
        print(board[i][j], end='')
    print()
