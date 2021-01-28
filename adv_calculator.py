def add(num1,num2):
	add=num1+num2
	return add	
	
def sub(num1,num2):
	sub=num1-num2
	return sub	
	
def mul(num1,num2):
	mul=num1*num2
	return mul	
	
def div(num1,num2):
	div=num1/num2
	return div

operator = ['+','-','*','/']

CalValue = input()
OperatorInput = []
for x in CalValue:
	if(x in operator):
		OperatorInput.append(x)
		CalValue = CalValue.replace(x,' ')
		
CalValue = CalValue.split(' ')
lenValue = len(OperatorInput)

for y in range(lenValue):
	if '*' in OperatorInput:
		index = OperatorInput.index('*')
		if CalValue[index+1] != '':
			cal = mul(int(CalValue[index]),int(CalValue[index+1]))
			CalValue[index+1] = cal
			CalValue[index] = ''
			OperatorInput[index] = '#'
		#print(index,CalValue)
	elif '/' in OperatorInput:
		index = OperatorInput.index('/')
		if CalValue[index+1] != '':
			cal = div(int(CalValue[index]),int(CalValue[index+1]))
			CalValue[index+1] = cal
			CalValue[index] = ''
			OperatorInput[index] = '#'
		elif CalValue[index + 1] == '':
			cal = sub(int(CalValue[index]), int(CalValue[index + 2]))
			CalValue[index + 2] = cal
			CalValue[index] = ''
			OperatorInput[index] = '#'
		#print(index,CalValue)
	if OperatorInput[y] == '+':
		index = OperatorInput.index('+')
		if CalValue[index+1] != '':

			cal = add(int(CalValue[index]),int(CalValue[index+1]))
			CalValue[index+1] = cal
			CalValue[index] = ''
			OperatorInput[index] = '#'
		elif CalValue[index + 1] == '':
			cal = add(int(CalValue[index]), int(CalValue[index + 2]))

			CalValue[index + 2] = cal
			CalValue[index] = ''
			OperatorInput[index] = '#'
		#print(index,CalValue)
	elif OperatorInput[y] == '-':
		index = OperatorInput.index('-')
		if CalValue[index+1] != '':
			cal = sub(int(CalValue[index]),int(CalValue[index+1]))
			CalValue[index+1] = cal
			CalValue[index] = ''
			OperatorInput[index] = '#'
		elif CalValue[index + 1] == '':
			cal = sub(int(CalValue[index]), int(CalValue[index + 2]))
			CalValue[index + 2] = cal
			CalValue[index] = ''
			OperatorInput[index] = '#'
		#print(index,CalValue)
for z in CalValue:
	if z != '':
		print(z)
