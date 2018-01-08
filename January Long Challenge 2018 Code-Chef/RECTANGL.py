t = int(raw_input())
while t>0:
    a,b,c,d = (int(x) for x in raw_input().strip().split(' '))
    if ((a==b) and (c==d) ) or ( a == c and b==d) or (a==d and b==c):
        print "YES"
    else:
        print "NO"
    t-=1
