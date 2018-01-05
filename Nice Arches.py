m = int(raw_input())
c = 0
while m > 0:
    s = raw_input()
    i = 0
    arr = []
    top = -1
    while i < len(s):
        if top == -1:
            arr.append(s[i])
            top+=1
        elif arr[top] == s[i]:
            arr.pop(top)
            top-=1
        elif arr[top]!=s[i]:
            arr.append(s[i])
            top+=1
        i+=1
    if len(arr)==0:
        c+=1
    m-=1
print c
