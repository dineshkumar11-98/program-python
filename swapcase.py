def swapcase1(a):
	l=len(a)
	ua=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	la=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	for gb in range(l):
		for x in range(26):
			if(a[gb]==ua[x]):
				print(la[x],end='')
			elif(a[gb]==la[x]):
				print(ua[x],end='')
			
ab=input()
swapcase1(ab)