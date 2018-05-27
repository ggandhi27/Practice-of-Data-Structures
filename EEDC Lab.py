n = int(raw_input())
arr = [x for x in raw_input().strip().split(' ')]
q = int(raw_input())
while q > 0:
    l,r = (int(x) for x in raw_input().strip().split(' '))
    l = l-1
    c = 0
    for x in range(l,r):
        Left = "".join(arr[0:x])
        Right = "".join(arr[x+1:n])
        if Left == "":
            Left = 0
        else:
            Left = int(Left)
        if Right == "":
            Right = 0
        else:
            Right = int(Right)
        s = Left + Right
        if (s%2 == 0 and s%3==0 and s%5 == 0):
            c+=1
    print c
    q-=1

