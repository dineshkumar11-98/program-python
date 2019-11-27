import mysql.connector
import time
print("*******************************************WELCOME*************************************")
print("                                        This is MYSQL\n                                ")
user = input("Enter the username:")
passw = input("Enter the password:")
data = input("Enter the database name:")
conn = mysql.connector.connect(user=user,password=passw,database=data)
s = conn.cursor()


def q():
    query = input("Enter your code:\n")
    s.execute(query)
    vis = input("could you like to see the changes:")
    if vis == "yes":
        try:
            print(s.fetchall())
        except:
            print("it give some error")
            print("this is only used to command like select or show..ect")
            print("Not for the command like insert delete..etc,so enter as no for like this command ")

            time.sleep(5)


    elif vis == 'no':
        print("process successfully complete")
    conn.commit()
    s.close()
q()
