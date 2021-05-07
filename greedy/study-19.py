#https://www.acmicpc.net/problem/5545
# check 
n = int(input())
a, b = map(int,input().split())
max_ = 0
c = []
base = int(input())
for i in range(n):
    c.append(int(input()))
c.sort(reverse=True)
c.insert(0, 0)
d = 0
for i in range(len(c)):
    d += c[i]
    if (base + d)//(a + b*i) >= max_:
        max_ = (base + d)//(a + b*i)
print(max_)