#https://www.acmicpc.net/problem/9375

tc = int(input())
for i in range(tc):
    n = int(input())
    if n == 0:
        print(0)
        continue
    fashion = dict()
    for j in range(n):
        a, b = input().split() # a =  hat, b = headgear
        if b in fashion.keys():
            fashion[b] += 1   # 딕셔너리에 있는경우 +1
        else:
            fashion[b] = 1 # 없는경우 1
        answer = 1
        for k in fashion.keys(): # tc : (3*2) -1
            answer *= fashion[k] + 1
    print(answer - 1)

