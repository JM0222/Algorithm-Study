#https://www.acmicpc.net/problem/1654
k, n = map(int, input().split())
lan = []
for i in range(k):
    lan.append(int(input()))
start = 1
end = max(lan)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lan:
        cnt += i // mid
    if (cnt) >= n:
        start = mid + 1
    elif (cnt) < n:
        end = mid - 1 
print(end)