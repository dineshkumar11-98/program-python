a,b=input().split()
a=int(a)
b=int(b)
c=0
for y in [x for x in range(a,b+1) if(x%2!=0)]:
	c=c+y
print(c)
