# https://www.acmicpc.net/problem/5567
# check
# https://richard25.tistory.com/44
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    m = int(input())
    friend = dict()

    for i in range(1, N+1) :
        friend[i] = []
    
    for _ in range(m) :
        a, b = map(int, input().split(" "))
        friend[a].append(b)
        friend[b].append(a)
    
    ans_set = set(friend[1])
    for i in friend[1] :
        ans_set.update(friend[i])
    print(len(ans_set) - 1)

# ===========================================
# https://li-fo.tistory.com/49
import sys
from collections import deque

def bfs(x):
    visited = [0] * n
    visited[x] = 1
    q.append(x)
    while q:
        x = q.popleft()
        for i in friends[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
    return visited


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
friends = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a-1].append(b-1)
    friends[b-1].append(a-1)

q = deque()
cnt = 0

res = bfs(0)
for res_ in res:
    if 1 < res_ <= 3:   # 1 : 본인, 2 : 친구, 3 : 친구의 친구
        cnt += 1
print(cnt)