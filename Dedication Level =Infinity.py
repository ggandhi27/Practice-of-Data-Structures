n = int(raw_input())
arr = []
dic = dict()
i = 0
while i<n:
    a,b = (raw_input().strip().split(' '))
    b = int(b)
    dic[b] = a
    arr.append(b)
    i+=1

arr.sort()
i=n-1
while i>n-4:
    print dic[arr[i]]
    i-=1
