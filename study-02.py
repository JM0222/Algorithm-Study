#TEST CASE
# n  cnt
# 6   8
# 16  4
#626331	-1

n = 626331

cnt = 0

while 1:
    if n == 1:
        break
    elif cnt >= 500: # cnt >= 500 이상일때 cnt = -1 후 break
        cnt = -1
        break
    else:
        if n%2 == 0: # 짝수일경우 
            n = n//2
            cnt += 1
        else: # 홀수일경우
            n = (n*3) + 1
            cnt += 1
print(cnt)