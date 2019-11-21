a,b=input().split()
a=int(a)
b=int(b)
c=1
d=1
for x in range(1,a+1):
    c=c*x
e=a-b
for y in range(1,e+1):
    d=d*y
f=c/d
print(int(f))
