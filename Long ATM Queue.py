n = int(raw_input())
heights = [int(x) for x in raw_input().strip().split(' ')]
i = 1
c = 1
while i < n:
    if heights[i]<heights[i-1]:
        c+=1
    i+=1
print c
