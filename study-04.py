a = 'ababababa'
b = 'aba'
len_a = len(a)
len_b = len(b)
i = 0
answer = 0
while i <= len_a - len_b:
    if a[i:i+len_b] == b:
        answer += 1
        i += len_b
    else:
        i += 1
print(answer)
