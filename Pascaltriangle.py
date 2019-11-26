a=int(input("Enter the row number: "))
l=[0,1,0]
lis=[]
z=a
t=a+1
k=" "*t
print(k,"1")
for y in range(a):
	le=len(l)
	for x in range(le):
		if(x+1<=le-1):
			s=l[x]+l[x+1]
			lis.append(s)
	r=" "*z
	print(r,*lis)
	l=[0,*lis,0]
	lis=[]
	z=z-1
