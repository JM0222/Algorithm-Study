#https://www.acmicpc.net/problem/3135
# check 


s, e = map(int,input().split())
n = int(input())
wish = []
b = 1000 # min 값을 찾기위한 수 
cnt = 0
for i in range(n):
    wish.append(int(input()))
for i in range(len(wish)):
    if abs(wish[i] - e) < b:
        b = abs(wish[i] - e) # wish 리스트중 min 값으로 b 세팅
if abs(s-e) <= b:  # 한칸씩이동해서 가는게 더 빠른경우
    cnt += abs(s-e)
else: # 아닐경우 즐겨찾기 이동후 +b
    cnt += 1
    cnt += b
print(cnt)