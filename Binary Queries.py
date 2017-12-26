N,Q=raw_input().strip().split(' ')
N,Q=(int(N),int(Q))
arr=[int(x) for x in raw_input().strip().split(' ')]
while Q != 0:
    query = [int(a) for a in raw_input().strip().split(' ')]
    if len(query) == 2:
        if arr[query[1]-1] == 0:
            arr[query[1]-1]=1
        else:
            arr[query[1]-1]=0
    else:
        a=arr[query[2]-1]
        if a == 0:
            print 'EVEN'
        else:
            print 'ODD'
    Q-=1
