l=list()
d=dict()
n=int(input('Enter no. of terms'))
if(n==1):
    l=[0]
    d={1:0}
elif(n==2):
    l=[0,1]
    d={1:0,2:1}
else:
    t1=0
    t2=1
    t3=0
    for x in range(1,n+1):
        l.append(t1) 
        d[x]=t1
        t3=t1+t2
        t1=t2
        t2=t3
print(l,'\n',d)
