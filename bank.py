def widthraw(n,account_number,name,balance,from_acc_num,amount):
    for check_w in range(n):
        #check the account number
        if account_number[check_w] == from_acc_num:
            #check the balance
            if balance[check_w] >= int(amount):
                balance[check_w] -= int(amount)
    

def deposite(n,account_number,name,balance,from_acc_num,amount):
    for check_w in range(n):
        #check the account number
        if account_number[check_w] == from_acc_num:
            balance[check_w] += int(amount)
    

def transfer(n,account_number,name,balance,from_acc_num,to_acc_num,amount):
    for check_w in range(n):
        if account_number[check_w] == from_acc_num:
            if balance[check_w] >= int(amount):
                balance[check_w] -= int(amount)
    for check_w in range(n):
        #check the account number
        if account_number[check_w] == to_acc_num:
            balance[check_w] += int(amount)
            
        
n = int(input('Number account want to create in integer: '))
n1 = 0
account_number = []
name = []
balance = []
print('\nAccount-number,Name,Balance\nExample input format: 001 John 10000\n\n')
for assin in range(n):
 account_numberi,namei,balancei = input('Account:'+str(assin+1)+'\nEnter the detail: ').split()
 account_number.append(account_numberi)
 name.append(namei)
 balance.append(int(balancei))

activitydata = input('\n1->Widthraw money from account\n   Format:Option Account number Amount\n   Example fomat:1 001 50 \n\n2->Deposite money to account\n   Format:Option Account number Amount\n   Example fomat:2 001 50 \n\n3->Transfer the money to other account\n   Format:Option Account number Other\'s account number Amount\n   Example fomat:3 001 002 50 \n\n Enter the detail:').split()


#check the choice
if int(activitydata[0]) == 1:
    widthraw(n,account_number,name,balance,activitydata[1],activitydata[2])
elif int(activitydata[0]) == 2:
    deposite(n,account_number,name,balance,activitydata[1],activitydata[2])
elif int(activitydata[0]) == 3:
    transfer(n,account_number,name,balance,activitydata[1],activitydata[2],activitydata[3])

for result in range(n):
    print('\nAccount no:',account_number[result],'\nName:',name[result],'\nAvaliable balance:',balance[result],'\n')
