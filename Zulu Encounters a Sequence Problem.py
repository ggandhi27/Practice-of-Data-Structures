t = int(raw_input())
while t>0:
    n = int(raw_input())
    arr = [int(x) for x in raw_input().strip().split(' ')]
    m = 0
    i = 0
    while i<n:
        l = i
        r = i
        if (i+1)<n:
            if arr[i+1] <=arr[i]:
                f=0
                while r<n:
                    if arr[r]<=arr[r+1]:
                        r+=1
                    else:
                        f=1
                        break
                if f==0:
                    r-=1
            elif arr[i+1] >=arr[i]:
                f=0
                while r<n:
                    if arr[r]>=arr[r+1]:
                        r+=1
                    else:
                        f=1
                        break
                if f==0:
                    r-=1
        if (i-1)>=0:
            if arr[i-1]<=arr[i]:
                f=0
                while l>=0:
                    if arr[l-1]<=arr[l]:
                        l-=1
                    else:
                        f=1
                        break
                if f==0:
                    l+=1
            elif arr[i-1]>=arr[i]:
                f=0
                while l>=0:
                    if arr[l-1]>=arr[l]:
                        l-=1
                    else:
                        f=1
                        break
        m = max(m,max(abs(arr[l]-arr[i]),abs(arr[l]-arr[r])))
        i+=1
    print m
    t-=1

