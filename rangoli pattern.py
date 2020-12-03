a=int(input())
b=[]
for i in range(a):
    b.append(chr(97+i))
s=4*a-3
t=(s-1)/2
b.reverse()
for i in range(a):
    print("-"*(int((s-1)/2)),end="")
    for j in range (0,i+1):
        print(b[j],end="-")
    b.reverse()
    for j in range(i,0,-1):
        if j==1 and i==a-1:
            print(b[-j],end="")
        else:    
            print(b[-j],end="-")
    b.reverse()
    print("-"*int((t)-1))
    s-=4
    t-=2
r=2
g=1
for i in range(a-1,0,-1):
    print("-"*r,end="")
    for j in range(1,i):
        print(b[j-1],end="-")
    b.reverse()
    for j in range(g,len(b)):
      print(b[j],end="-")
    b.reverse()
    print("-"*(r-1))
    r+=2
    g+=1