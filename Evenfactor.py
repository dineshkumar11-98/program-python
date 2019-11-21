a=input()
a=int(a)
for x in range(1,a+1):
	if(a%x==0):
		if(x%2==0):
			print(x,end=' ')
