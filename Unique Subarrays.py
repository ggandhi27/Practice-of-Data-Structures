t = int(raw_input())
while t>0:
    i=0
    j=0
    n = int(raw_input())
    arr = [int(x) for x in raw_input().strip().split(' ')]
    s=0
    while i<n:
        j=i
        while j<n:
            dic = {}
            f=0
            for x in  arr[i:j+1]:
                if x in dic:
                    f=1
                    break
                else:
                    dic[x]=1
            if f==0:
                s+= (j-i+1)
            j+=1
        i+=1
    print s
    t-=1
