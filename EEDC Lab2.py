n = int(raw_input())
arr = [int(x) for x in raw_input().strip().split(' ')]
q = int(raw_input())
su = sum(arr)
while q > 0:
    l,r = (int(x) for x in raw_input().strip().split(' '))
    l = l-1
    c = 0
    for x in range(l,r):
        s = su - arr[x]
        if (s%2 == 0 and s%3==0 and s%5 == 0):
            c+=1
    print c
    q-=1

