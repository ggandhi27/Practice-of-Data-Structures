n = int(raw_input())
arr = [int(x) for x in raw_input().strip().split(' ')]
q = int(raw_input())
while q > 0:
    l,r = (int(x) for x in raw_input().strip().split(' '))
    i=l
    while i<=r:
        arr[i-1],arr[n-i]=arr[n-i],arr[i-1]
        i+=1
    q -= 1
for x in arr:
    print x,
