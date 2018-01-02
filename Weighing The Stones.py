t = int(raw_input())
while t>0:
    n = int(raw_input())
    rupam = [int(x) for x in raw_input().strip().split(' ')]
    ankit = [int(x) for x in raw_input().strip().split(' ')]
    r = dict()
    a = dict()
    mr = 0
    mmr = None
    for x in rupam:
        try:
            r[x] = r[x] + 1
            if r[x]>mr:
                mr = r[x]
                mmr = x
            elif r[x] == mr :
                if x>mmr:
                    mmr = x
        except KeyError:
            r[x] = 1
            if mmr == None:
                mmr = x
                mr = 1
            if mr == 1:
                if x > mmr:
                    mmr = x
    ma = 0
    mma = None
    for x in ankit:
        try:
            a[x] = a[x] + 1
            if a[x]>ma:
                ma = a[x]
                mma = x
            elif a[x] == ma :
                if x>mma:
                    mma = x
        except KeyError:
            a[x] = 1
            if mma == None:
                mma = x
                ma = 1
            if ma == 1:
                if x > mma:
                    mma = x
    if mma > mmr:
        print "Ankit"
    elif mma == mmr:
        print "Tie"
    else:
        print "Rupam"
    t-=1
