t = int(raw_input())
while t > 0:
    n = int(raw_input())
    arr = [int(x) for x in raw_input().strip().split(' ')]
    arr.sort()
    c = arr.count(arr[0])
    if c%2 == 0:
        print "Unlucky"
    else:
        print "Lucky"
    t-=1
