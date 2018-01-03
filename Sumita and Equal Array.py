t = int(raw_input())
while t>0:
    n,x,y,z=(int(ax) for ax in raw_input().strip().split(' '))
    arr = [int(ax) for ax in raw_input().strip().split(' ')]
    i = 0
    while i<n:
        while arr[i]%x == 0:
            arr[i] = arr[i]/x

        while arr[i]%y == 0:
            arr[i] = arr[i]/y

        while arr[i]%z == 0:
            arr[i] = arr[i]/z
        
        i+=1
    i=1
    f=0
    while i<n:
        if arr[i]!=arr[i-1]:
            f=1
            break
        i+=1
    if f==1:
        print "She can't"
    else:
        print "She can"
    t-=1
