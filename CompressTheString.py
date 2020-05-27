n = list(input())
nt = []
ct = []
c = 1
for i in range(len(n)):
    if(i!=len(n)-1):
        if(n[i+1]==n[i]):
            c+=1
        else:
            nt.append(int(n[i]))
            ct.append(c)
            c = 1
    else:
        nt.append(int(n[i]))
        ct.append(c)
t = list(zip(ct,nt))

for i in t:
    print(i, end = ' ')
