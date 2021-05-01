# https://www.acmicpc.net/problem/9012

# 시간: 20분 
n = int(input())
def vps(a):
    stack = []
    for i in a: # 문자열 순회하면서 '(' 나오면 스택에 append)
        if i == "(":
            stack.append(i)
        else:
            if stack:  # ')' 나오면 pop (스택이 존재할경우)
                stack.pop()
            else:
                print("NO")
                return
    if stack: # 스택이 남아있다면
        print("NO")
        return
    else: # 다 비워지면 
        print("YES") 
        return

for i in range(n):
    a = input()
    vps(a)