a=input()
b=''
c=''
l=len(a)
i=0
while(i<l):
    if(i%2==0 or i==0):
        b=b+a[i]
        i=i+1
    else:
        c=c+a[i]
        i=i+1

l1=len(b)
l2=len(c)
i1=0

while(i1<l1 and i1<l2):
    print(c[i1]+b[i1],end='')
    i1+=1
