a,b=input().split()
a=int(a)
b=int(b)
d=1
e=1
for x in range(b):
	d=d*a
	a=a-1
for y in range(1,b+1):
	e=e*y
z=d/e
print(round(z))
