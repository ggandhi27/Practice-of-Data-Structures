t = int(raw_input())
while t>0:
    n,m = (int(x) for x in raw_input().strip().split(' '))
    arr = []
    i = 0
    while i<n:
        arr.append(list(raw_input()))
        i+=1
    st = raw_input()
    i = 0
    j = 0
    while i < len(st):
        if not (st[i] in arr[j]):
            print "No"
            break
        else:
            arr[j].pop(arr[j].index(st[i]))
            j = (j+1)%n
            i+=1
    if i==len(st):
        print "Yes"
    t-=1
