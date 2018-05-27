n = int(raw_input())
arr = [int(x) for x in raw_input().strip().split(' ')]
s = sum(arr)
print s
if s%n !=0:
    print (s+(s%n))/n
else:
    print (s/n)+1
