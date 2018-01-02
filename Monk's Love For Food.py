q = int(raw_input())          # Reading input from STDIN

arr = []

while q>0:
        a = [int(x) for x in raw_input().strip().split(' ')]
        if len(a) == 1:
              if len(arr) == 0:
                      print "No Food"
              else:
                      print arr.pop()
        else:
              arr.append(a[1])
              q-=1
