def ams(a):
  l=len(a)
  s=0
  for x in range(l):
    s=s+int(a[x])**3
  if(s==int(a)):
    print("yes")
  else:
    print('no')
    

a=input()
ams(a)
