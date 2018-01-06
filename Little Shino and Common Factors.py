a,b = (int(x) for x in raw_input().strip().split(' '))
i=1
m = int(a**(1/2.0)) + 1
s = 0
dic = {}
while i <= m:
    if a%i==0 :
        if a/i == i:
            dic[i]=1
        else:
            dic[i]=1
            dic[a/i]=1
    i+=1

m = int(b**(1/2.0)) + 1
i=1
dic2 = {}
while i<=m:
    if b%i==0:
        if b/i == i:
            if i in dic and i not in dic2:
                dic2[i] = 1
                s+=1
        else:
            if i in dic and i not in dic2:
                dic2[i] = 1
                s+=1
            if b/i in dic and b/i not in dic2:
                dic2[i] = 1
                s+=1
    i+=1
print s
