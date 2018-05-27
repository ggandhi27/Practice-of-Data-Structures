t = int(raw_input())
while t>0:
    n,k = (int(x) for x in raw_input().strip().split(' '))
    arr = [int(x) for x in raw_input().strip().split(' ')]
    sa = sum(arr)
    if sa >= 0:
        i=0
        while i<n and arr[i]>=0:
            sa=sa+arr[i]
            i+=1
        i=n-1
        while i>=0 and arr[i]>=0:
            sa=sa+arr[i]
            i+=1
    
    t-=1
