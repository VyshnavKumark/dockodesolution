p=int(input())
q=int(input())
b=[[0]*q for _ in range(p)]
d=1
for i in range(1,(q*p)+1):
    td=max(0,i-p)
    count=min(i,(p-td),p)
    for j in range(0,count):
        b[min(p,i)-j-1][td+j]=d
        d+=1
for x in b:
    for i in x:
        print(i,end=" ")
    print()
