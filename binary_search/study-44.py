#https://www.acmicpc.net/problem/2805
#check
n, m = map(int,input().split())
tree = list(map(int,input().split()))
start = 1
end = max(tree)
while start <= end:
    mid = (start + end) // 2
    sum_tree = 0
    for i in tree:
        k = i - mid
        if k > 0:
            sum_tree += k
    if sum_tree >= m:
        start = mid + 1
    else:
        end = mid -1
print(end)