a=1
l=[]
v=' '
c=5
print("        1")
for x in range(6):
        a=a+1
        l.append(a)
        d=v*c
        print(d,"1",*l,"1",sep=' ')
        c=c-1
b=len(l)
f=0
for y in range(6):
        e=v*f
        print(e,"1",*l[:b:1],"1",sep=' ')
        b=b-1
        f=f+1
print("        1")
