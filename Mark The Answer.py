n,a = (int(x) for x in raw_input().strip().split(' '))
arr = [int(x) for x in raw_input().strip().split(' ' )]
c = 0
f = 0
for x in arr:
    if x <= a :
        c += 1
    elif x > a and f == 0:
        f = 1
    elif x > a and f == 1:
        break
print c
