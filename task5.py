n = input()
if len(n) < 3:
    print(n)
elif n[-3:] == 'ing':
    print(n+'ly')
else :
    print(n + 'ing')
