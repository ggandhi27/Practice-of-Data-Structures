t = int(raw_input())
while t > 0:
    n,k = (int(x) for x in raw_input().strip().split(' '))
    arr = [int(x) for x in raw_input().strip().split(' ')]
    k = k%n
    arr1 = [0]*n
    i = 0
    while i < n:
        arr1[(i+k)%n] = arr[i]
        i+=1
    for x in arr1:
        print x,
    print ""
    t-=1
