t = int(raw_input())
while t>0:
    n = int(raw_input())
    arr = []
    i = 0
    while i<n:
        arr1 = [int(x) for x in raw_input().strip().split(' ')]
        arr1.sort()
        arr.append(arr1)
        i+=1
    i=n-1
    s=0
    l = arr[n-1][n-1]
    s=s+l
    f=1
    while i>0:
        j=n-1
        while arr[i-1][j]>=l and j>=0:
            j-=1
        if j==-1:
            print "-1"
            f=0
            break
        else:
            l=arr[i-1][j]
            s=s+l
        i-=1
    if f==1:
        print s
    t-=1
