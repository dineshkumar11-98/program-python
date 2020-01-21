l=int(input())
a=input().split()
z=a[0]
for x in range(l):
	for y in range(l):
		if(z>a[y]):
			z=a[y]
co=a.count(z)
if(co%2!=0):
	for i in range(2,13):
		if(co%i!=0 and co!=1):
			print('lucky')
			break
		else:
			print('normal')
elif(co%2==0):
			print('unlucky')