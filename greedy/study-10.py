#https://www.acmicpc.net/problem/2839
a = int(input())
box = 0
while True:
  if a%5 ==0:  # 5이 배수이면 몫만큼 더해주고 break
    box = box + (a//5)
    print(box)
    break
  a = a - 3  # 아닐경우 -3 해준다음 box 1더해주기
  box += 1
  if a < 0: # case 벗어난경우
    print("-1")
    break