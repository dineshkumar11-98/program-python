a,b,c=input().split()
a=int(a)
b=int(b)
i=0
for x in range(a,b+1):
	if(c in str(x)):
		i=i+1
print(i)
