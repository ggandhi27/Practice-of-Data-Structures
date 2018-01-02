n,k = (int(x) for x in raw_input().strip().split(' '))
arr = [int(x) for x in raw_input().strip().split(' ')]
i = 0
maxArray = []
while i<=(n-k):
    maxArray.append(max(arr[i:i+k]))
    i+=1

for x in maxArray:
    print x,
