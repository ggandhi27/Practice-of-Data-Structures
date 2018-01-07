n = int(raw_input())
l = 1
u = n
f = 0
while l<=u:
    mid = (l+u)/2
    if n == mid*mid:
        print "YES"
        f = 1
        break
    else:
        if mid*mid<n:
            l = mid+1
        else:
            u = mid - 1

if f==0:
    print "NO"
