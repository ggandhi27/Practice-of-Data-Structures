t = int(raw_input())
while t > 0:
    n = int(raw_input())
    arr = dict()
    i = 1
    a = [int(x) for x in raw_input().strip().split(' ')]
    while i <= n:
        arr[a[i-1]] = i
        i+=1

    q = int(raw_input())
    while q > 0:
        x = int(raw_input())
        try:
            print arr[x]
        except KeyError:
            print -1
        q-=1
    t-=1
