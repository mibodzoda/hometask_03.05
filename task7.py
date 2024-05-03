n = input()
m = input()
sent = n.split()
cnt = 0
for i in sent:
    if i == m:
        cnt+=1
print(cnt)