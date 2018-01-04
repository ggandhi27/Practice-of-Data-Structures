n,q = (int(x) for x in raw_input().strip().split())
arr = list(raw_input())
while q>0:
    l,r,k = (int(x) for x in raw_input().strip().split())
    m='z'
    l-=1
    arr1 = [0]*26
    if k<(r-l+1):
        while l<r:
            arr1[ord(arr[l])-97]+=1
            l+=1
        i=0
        while i<26:
            if arr1[i]!=0:
                k-=1
                if k==0:
                    print chr(i+97)
                    break
            i+=1
    else:
        print "Out of range"

    q-=1

