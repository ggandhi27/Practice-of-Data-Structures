n = int(raw_input())
arr = [int(x) for x in raw_input().strip().split(' ')]
di = dict()
m,c = 0,0
for x in arr:
    try:
        di[x] = di[x] + 1
        if di [x] > c:
            c = di[x]
            m = x
        elif di[x] == c:
            if x < m:
                m = x
    except KeyError:
        di[x] = 1

print m
