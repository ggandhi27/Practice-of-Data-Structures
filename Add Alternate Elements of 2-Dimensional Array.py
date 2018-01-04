arr = [int(x) for x in raw_input().strip().split()]
i = 0
s1 = 0
s2 = 0
while i<len(arr):
    if i%2 == 0:
        s1 += arr[i]
    else:
        s2 += arr[i]
    i+=1
print s1
print s2
