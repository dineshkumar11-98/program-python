import time
#get the name
def nam():
	try:
		name=str(input("Enter your name:"))
	except:
		print("Enter the valid name,")
		time.sleep(3)
		return nam()
	return name
#get the contact number
def ph():
	try:
		phone=int(input("Enter your contact number:"))
		ph1=str(phone)
		lent=len(ph1)
		if(lent<10 or lent > 10):
			print("contact number should be 10 digit")
			time.sleep(3)
			return ph()
	except:
		print("Contact number should be numerical")
		time.sleep(3)
		return ph()
	return phone
#get source and destination
def sode():
	try:
		print("Enter the source and destination")
		source=float(input('Start point:'))
		
		#check empty variable
		if(source==""):
			print("Enter valid source & destination")
			return sode()
		#check source and destination are greater than 0
		if(source<0):
			print("source should not less than 0")
			return sode()
		#check destination are greater than 0
		destination=float(input("end point:"))
		if(destination<=0):
			print("Destination should not less than or equal to 0")
			return sode()
		#check source and destination are equal are not
		if(source==destination):
			print("source and destination should be different")
			return sode()
		#find distance
		if(source<destination):
			distance=destination-source
		elif(source>destination):
			print("invalid source & destination")
			time.sleep(3)
			return sedo()
	except:
		print("source and destination not in numeric or invalid data")
		return sode()
	return distance
#get class option
def cls():
	try:
		print("choose the class for travel")
		print("1->car-20rs/km\n2->auto-15rs/km \n3->bike-8rs/km")
		choise=int(input("class:"))
		if(choise>3):
			print("Enter valid option")
			return cls()
		if(choise==1):
			kp=20
		elif(choise==2):
			kp=15
		elif(choise==3):
			kp=8
	except:
		print("enter valid option")
		time.sleep(3)
		return cls()
	return kp
#calculation
def cal():
	price=sode()*cls()
	return price
print("********************DETAIL********************")
print(" Your name is:",nam(),"\n","Your contact number is:",ph(),"\n","Total amount",cal(),"rs")