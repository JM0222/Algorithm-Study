#https://www.acmicpc.net/problem/17219


n, m = map(int, input().split())
l = dict()
for i in range(n):
    a, b = input().split()
    l[a] = b
for i in range(m):
    c = input()
    print(l[c])