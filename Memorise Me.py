n = int(raw_input())
arr = [int(x) for x in raw_input().strip().split(' ')]
b = [0]*1001
for x in arr:
    b[x]+=1
q = int(raw_input())
while q !=0:
    n = int(raw_input())
    if b[n]!=0:
        print b[n]
    else:
        print "NOT PRESENT"
    q-=1
