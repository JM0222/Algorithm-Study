#a = ['bat','apple','ant']

# a = ['acb','abb','aab']
# a.sort()


a = []
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n):
            words = input()
            a.append(words)
        a.sort()
        print(a[0])
        a.clear()
