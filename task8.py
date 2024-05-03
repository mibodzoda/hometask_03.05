n = input()
a = []
for i in range(len(n)):
    if n[i] != n[i-1]:
        a.append(n[i])
print(''.join(a))
