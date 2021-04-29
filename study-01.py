#https://programmers.co.kr/learn/courses/30/lessons/12901

# TEST CASE
a= 5
b= 24
answer=''

# 2016년 
year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# ex 2월 1일은 32
day = sum(year[:a]) - (year[a-1]-b)

if day%7 == 6:
    answer='WED'
elif day%7 == 0:
    answer='THU'
elif day%7 == 1:
    answer='FRI'
elif day%7 == 2:
    answer='SAT'
elif day%7 == 3:
    answer='SUN'
elif day%7 == 4:
    answer='MON'
elif day%7 == 5:
    answer='TUE'    
print(answer)