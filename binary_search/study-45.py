#https://www.acmicpc.net/problem/2512
#check
n = int(input())
city = list(map(int,input().split()))
budget = int(input())
start = 1
end = max(city)
while start <= end:
    mid = (start + end) // 2
    sum_city = 0
    for i in city:
        if mid >= i:
            sum_city += i
        else:
            sum_city += mid
    if sum_city <= budget:
        start = mid + 1
    else:
        end = mid - 1
print(end)
