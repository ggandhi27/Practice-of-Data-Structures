t = int(raw_input())
while t>0:
    n,a,b,c = (int(x) for x in raw_input().strip().split(' '))
    count = (n/a) + (n/b) + (n/c) - (n/(a*b)) - (n/(b*c)) - (n/(a*c))# + (n/(a*b*c))
    print count
    t-=1
