import sys
t = int(raw_input())
while t>0:
    n = int(raw_input())
    arr = [int(x) for x in raw_input().strip().split(' ')]
    i = 0
    maxa = 0
    maxb = 0
    mina = sys.maxint
    minb = sys.maxint
    while i < n:
        x = arr[i]+i
        y = arr[i]-i
        if x > maxa:
            maxa=x
        if x < mina:
            mina=x
        if y>maxb:
            maxb=y
        if y<minb:
            minb=y
        i+=1
    print max(maxa-mina,maxb-minb)
    t-=1
