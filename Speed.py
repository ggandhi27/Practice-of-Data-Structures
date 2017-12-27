t = int(raw_input())
while t > 0:
    n = int(raw_input())
    arr = [int(x) for x in raw_input().strip().split(' ')]
    i = 1
    c = 1
    while i < n:
        if arr[i] < arr[i-1]:
            c+=1
        i+=1
    print c
    t-=1
