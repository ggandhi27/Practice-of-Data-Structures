t = int(raw_input())
while t > 0:
    n = int(raw_input())
    arr = [int(x) for x in raw_input().strip().split(' ')]
    arr.sort()
    i = 0
    while i < n:
        if i!=n-1:
            if arr[i] == arr[i+2]:
                i+=3
            else:
                print arr[i]
                break
        else:
            print arr[i]
            break
    t-=1
