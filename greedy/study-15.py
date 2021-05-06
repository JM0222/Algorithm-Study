#https://www.acmicpc.net/problem/2872
n = int(input())
a = []
cnt = 0
for i in range(n):
    a.append(int(input()))
max = a[0]
for i in range(1,n) : 
 if a[i] > max :
   if max+1 != a[i] :
     cnt +=1
   max = a[i]
 else :
   cnt +=1
print(cnt)