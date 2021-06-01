#https://www.acmicpc.net/problem/14496
from collections import deque
a, b = map(int,input().split()) 
n, m = map(int,input().split()) 
board = [[] for _ in range(n+1)]

def bfs(x, y):
    q = deque()
    visited = [0] * (n+1)
    visited[x] = 1
    q.append(x)
    while q:
        x = q.popleft()
        if x == y:
            return visited[x]
        for i in board[x]:
            if not visited[i]: # 방문안한 경우
                visited[i] = visited[x] + 1
                q.append(i)
    return -1
    
for i in range(m):
    c, d = map(int,input().split())
    board[c].append(d)
    board[d].append(c)
ans = bfs(a, b)
print(ans)