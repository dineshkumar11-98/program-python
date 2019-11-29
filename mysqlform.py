import mysql.connector


# connecting to database
name = input("Enter the user_name:")
password = input("Enter the password:")
db = input("Enter the database name:")
conn = mysql.connector.connect(user=name, password=password, database=db)
cur = conn.cursor()
# get the option to perform the action
print("select the option to perform the operation")
print("1->create database\n2->delete database\n3->create table\n4->delete table\n5->show the content of table\n6->insert data to table\n7->edit the content of table\n")
choise = int(input("Enter your choise:"))


# create database
def create_database():
    db_name = input("Enter the database name:")
    query = "create database %s;" % db_name
    cur.execute(query)
    print("database sucessfully created")


# delete database
def delete_database():
    db_name = input("Enter the database name")
    query = "drop database %s;" % db_name
    cur.execute(query)
    print("database sucessfully deleted")


# create table
def create_table():
    table_name = input("Enter the table name:")
    field = input("Enter the table field in same line seperated by coma',':")
    query = "create table %s(%s);" % (table_name, field)
    cur.execute(query)
    print("sucessfully table created")


# delete table
def delete_table():
    table_name = input("Enter the table name:")
    query = "drop table %s" % table_name
    cur.execute(query)
    print("table sucessfully deleted")


# show the content of the table
def show_content():
    table_name = input("Enter the table name:")
    query = "select * from %s" % table_name
    cur.execute(query)
    print(*cur.fetchall(),sep="\n")


# insert data to the table
def insert_content():
    print("NOTE:insert the data to table based on field and data type of the table")
    t_name = input("To know the field format of table give the table name")
    query = "desc %s" % t_name
    cur.execute(query)
    print(cur.fetchall())
    print(t_name)
    t_data = input("Enter the data based on field:")
    query1 = "insert into %s values(%s);" % (t_name, t_data)
    print(t_name, t_data)
    cur.execute(query1)
    conn.commit()
    print("sucessfull insert data to table")


# edit table data
def edit_data():
    t_name = input("Enter the table name:")
    change_data = input("Enter the new data with field name\ne.g field_name=new_data:")
    exist_data = input("Enter the old data with field name\ne.g field_name=old_data:")
    query = "update %s set %s where %s;" % (t_name, change_data, exist_data)
    cur.execute(query)
    conn.commit()


if (choise == 1):
    create_database()
elif (choise == 2):
    delete_database()
elif (choise == 3):
    create_table()
elif (choise == 4):
    delete_table()
elif (choise == 5):
    show_content()
elif (choise == 6):
    insert_content()
elif (choise == 7):
    edit_data()
conn.close()
