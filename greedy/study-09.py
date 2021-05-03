#https://www.acmicpc.net/problem/4796
# 20min
cnt = 1
while 1:
    answer = 0
    L, P, V = map(int,input().split())
    if L == 0 and P == 0 and V == 0:
        break
    answer += L * (V // P)
    # L이 나머지보다 작을경우 반드시 체크해줘야한다
    answer += min(L, V%P)  # ex 3 8 20 
    print("Case {0}: {1}".format(cnt, answer))
    cnt += 1