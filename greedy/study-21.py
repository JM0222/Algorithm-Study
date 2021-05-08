#https://www.acmicpc.net/problem/13417
from collections import deque

for _ in range(int(input())):
    N = int(input())
    li = deque(input().split())
    queue = deque(li.popleft())
    while li:
        t = li.popleft()
        print(t)
        if t > queue[0]:
            queue.append(t)

        else:
            queue.appendleft(t)

    print(''.join(queue))
