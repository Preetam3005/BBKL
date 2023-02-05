import salesproject  
import PRODUCT 
import datetime
import mysql.connector as sqltor
ofile = open("db.txt" , "a+")
data= ofile.read()
if len(data) == 0:
    password1= input("Enter password of your MySQL sever :")
    mycon=sqltor.connect(user= "root" , host= "localhost" ,  password= password1)
    cursor= mycon.cursor()
    database= input("enter name of database to be created : ")
    query1= "create database "+ database
    cursor.execute(query1)
    query2="use " + database
    cursor.execute(query2)
    query3= "create table salenew(PRODUCT_ID INT(5) PRIMARY KEY , PRODUCT_NAME VARCHAR(25) ,  QTY INT(2) ,PRICE INT(4) ,  DATE_OF_PURCHASE DATE )"
    cursor.execute(query3)
    mycon.commit()
    ofile.write( password1 + " " + database )
    print("Database successfully created. Please restart the program")
    ofile.close()
elif len(data)!= 0:
    print("1. Manage employee")
    print("2. Manage products")
    print("3. New purchase and Logs")
    ch = int(input("Enter your choice :"))
    if ch == 1:
        print("A. NEW EMPLOYEE")
        print("B.Employee count")
        print("C. Increament(salary)")
        print("D.Employee resign")
        ch2= input("Enter choice:(A,B,C,D) :")
        if ch2== "A" or ch2 == "a":
            print(salesproject.newemp())
        if ch2== "B" or ch2 == "b":
            print(salesproject.empcount())
        if ch2== "C" or ch2== "c":
            Eid= input("Enter Eid: ")
            inc= float(input("Enter the amput to be increased : "))
            salesproject.salinc(Eid , inc)
        if ch2== "D" or ch2=="d":
            Eid= input("Enter Eid: ")
            salesproject.resign(Eid)
    if ch== 2:
        print("E. New stock")
        print("F. Add Product(stock increment)")
        print("G. Sold")
        print("H. Increase price")
        print("I. Decrease price")
        ch3= input("Enter choice(E/F/G) :")
        if ch3== "E" or ch3=="e":
            print(PRODUCT.newstock())
        if ch3== "F" or ch3=="f":
            prid= int(input("Enter Product id : "))
            stock= int(input("Enter stock : "))
            if stock > 1:
                PRODUCT.add(prid , stock)
            else:
                PRODUCT.add(prid)
        if ch3 == "G" or ch3=="g":
            proid= int(input("Enter Product id : "))
            nos= int(input("Enter no of item bought of above product id :"))
            PRODUCT.sold(proid , nos)
        if ch3 ==  "H" or ch3=="h":
            pr= int(input("Enter Product id : "))
            inc= float(input("Enter amount to be increased :"))
            PRODUCT.incprc(pr, inc)
        if ch3== "I" or ch3== "i":
            rp= int(input("Enter Product id : "))
            dec= float(input("Enter amount to be increased :"))
            PRODUCT.Decprc(rp,dec)
    if ch== 4:
        with open("db.txt" ,  "r") as ifile:
            data= ifile.read()
            dnew= data.split()
            print(dnew)
            '''mycon= sqltor.connect( host="localhost", user= "root", database=data[1]  , password= data[0] )
            if mycon.is_connected():
                print("successfully connected")
            else:
                print("oops connection failed!!!!!")'''
        
        

        
        
        
        
    
