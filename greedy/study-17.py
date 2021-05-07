#https://www.acmicpc.net/problem/1758
n = int(input())
a = []
answer = 0
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
for i in range(len(a)):
    k = a[i] - i
    if k > 0:
        answer += k
print(answer)