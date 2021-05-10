#https://www.acmicpc.net/problem/19941
# n, k = map(int,input().split())
# a = input()
# l = []
# for i in range(len(a)):
#     l.append(a[i])
# print(l)
# answer = 0
# max_l = len(l) - k
# right = 0
# for i in range(len(l)):
#     if l[i] == "P":
#         if i >= max_l-1:
#             break
#         for j in range(i-k,i+k+1):
#             if l[j] == "H":
#                 l[j].replace("H","X")
#                 answer +=1
#                 break
# print(l)
# print(answer)

a = ["a","b"]
a.replace("a","A")
print(a)