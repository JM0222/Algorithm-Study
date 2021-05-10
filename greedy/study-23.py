#https://www.acmicpc.net/problem/15903
n, m = map(int, input().split())
a = list(map(int,input().split()))
a.sort()
while m:
    m -= 1
    k = a[0] + a[1]
    a[0] = k
    a[1] = k
    a.sort()
print(sum(a))