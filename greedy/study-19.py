#https://www.acmicpc.net/problem/5545
# check 
n = int(input())
a, b = map(int,input().split()) # 도우 , 토핑
max_ = 0 
c = []
base = int(input())
for i in range(n):
    c.append(int(input()))
c.sort(reverse=True)
c.insert(0, 0) # 0을 insert  [0,300, 100,50]
d = 0
for i in range(len(c)): 
    d += c[i] # d = 토핑의 합
    if (base + d)//(a + b*i) >= max_: # 열량 계산하면서 max값 갱신
        max_ = (base + d)//(a + b*i)
print(max_)
