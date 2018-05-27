n = int(raw_input())
s = []
i = 0
while n>0:
    nn = int(raw_input())
    if nn == 0:
        if len(s) == 0:
            pass
        else:
            s.pop()
    else:
        s.append(nn)
    n-=1
print sum(s)
