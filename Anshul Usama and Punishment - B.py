n = int(raw_input())
arr = [20,30,40,90,80,270]
i=7
while i<=n:
    if i%2==0:
        arr.append((3**(i/2))*10)
    else:
        arr.append((2**((i+1)/2))*10)
    i+=1
m=0
i=0
while i<n:
    j=0
    while j<n:
        if i!=j:
            m = max(m,abs(arr[i]+arr[j])+abs(arr[i]-arr[j]))
        j+=1
    i+=1
print m
