
a=input()
s=len(a)


d=int(a)
if(d<0):
	c=int(a[1])+int(a[s-1])
	if(c%4==0):
		print('Yes')
	else:
		print('No')
elif(d>0):
    e=int(a[s-2])+int(a[s-1])
    if(e%4==0 and e/4<1):
        print('Yes')
    else:
        print('No')
