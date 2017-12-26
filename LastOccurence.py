t = int(raw_input())
while t > 0:
    n = int(raw_input())
    arr = [int(x) for x in raw_input().strip().split(' ')]
    q = int(raw_input())
    while q > 0:
        nn = int(raw_input())
        i = 0
        p = -1
        while i < n:
            if arr[i] == nn:
                p = i
                break
            i+=1
        if p == -1:
            print p
        else:
            i = n-1
            while i > p:
                if arr[i] == nn:
                    p = i
                    break
                i -= 1
            print p+1
        q-=1
    t-=1
