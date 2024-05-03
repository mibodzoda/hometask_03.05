n = input()
cnt = {}
for i in n:
    if i in cnt:
        cnt[i.lower()] +=1
    else:
        cnt[i.lower()] = 1
print(cnt)