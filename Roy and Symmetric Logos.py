t = int(raw_input())
while t>0:
    n = int(raw_input())
    arr = []
    i = 0
    while i < n:
        arr.append(list(raw_input()))
        i+=1
    i=0
    j=0
    f=0
    while i<=n/2:
        j=0
        while j<=n/2:
            if not (arr[i][j] == arr[i][n-1-j] and arr[i][j] == arr[n-1-i][j] and arr[i][j] == arr[n-1-i][n-1-j]):
                f=1
                break
            j+=1
        i+=1
    if f==1:
        print "NO"
    else:
        print "YES"

    t-=1
