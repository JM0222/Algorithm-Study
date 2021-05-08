#https://www.acmicpc.net/problem/11508
n = int(input())
a = []
answer = 0
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
k = n // 3
answer = sum(a)
while k:
    answer -= a[3*k-1]
    k -= 1
print(answer)