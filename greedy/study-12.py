# https://www.acmicpc.net/problem/11497

# 50분 실패 
tc = int(input())
for i in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    answer = 0
    cnt = len(a) //2
    while cnt:
        if max(a[0]-a[2], a[0]-a[1]) > answer:
            answer = max(a[0]-a[2], a[0]-a[1])
            a.pop(0)
            cnt -= 1
        else:
            a.pop(0)
            cnt -= 1
    print(answer)
