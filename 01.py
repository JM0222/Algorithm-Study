m = int(input())
s = set()
for i in range(m):
    a = input()
    if "add" in a:
        s.add(int(a[4:]))
    elif "check" in a:
        if int(a[6:]) in s:
            print(1)
        else:
            print(0)
    elif "remove" in a:
        if int(a[7:]) in s:
            s.remove(int(a[7:]))
    elif "toggle" in a:
        if int(a[7:]) in s:
            s.remove(int(a[7:]))
        else:
            s.add(int(a[7:]))
    elif "all" in a:
        for i in range(1,21):
            s.add(i)
    elif "empty" in a:
        s.clear()