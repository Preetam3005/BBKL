import salesproject
import PRODUCT 
import mysql.connector as sqltor
import pickle
# db= "HALOALKANE"
ofile = open("db.txt" , "a+")
ofile.seek(0)
data= ofile.read()
if len(data) == 0:
    password1= input("Enter password of your MySQL sever :")
    ofile.write( password1)
    ofile.close()
     
    mycon=sqltor.connect(user= "root" , host= "localhost" ,  password= password1)
    cursor= mycon.cursor()
    
    query1= "create database haloalkane"
    cursor.execute(query1)
    query2= "use haloalkane"   
    cursor.execute(query2)
    query3= "create table salenew2(CPN varchar(11) , PRODUCT_ID INT(5) , PRODUCT_NAME VARCHAR(25) ,  QTY INT(2) ,PRICE INT(4) ,  DATE_OF_PURCHASE DATE )"
    cursor.execute(query3)
    mycon.commit()
    
    print("Database successfully created. Please restart the program")
    ofile.close()
elif len(data)!= 0:
    
    print("1. Manage employee")
    print("2. Manage products")
    print("3. New purchase and Logs")
    ch = int(input("Enter your choice :"))
    if ch == 1:
        #1. Manage employee
        print("A. NEW EMPLOYEE")
        
        print("B. Increament(salary)")
        print("C.Employee resign")
        ch2= input("Enter choice:(A,B,C) :")
        if ch2== "A" or ch2 == "a":
            print(salesproject.newemp())
        
        if ch2== "B" or ch2== "b":
            Eid= input("Enter Eid: ")
            inc= float(input("Enter the amput to be increased : "))
            salesproject.salinc(Eid , inc)
        if ch2== "C" or ch2=="c":
            Eid= input("Enter Eid: ")
            salesproject.resign(Eid)
    if ch== 2:
        #2. Manage products
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
    if ch== 3:
        #3. New purchase and Logs
        with open("db.txt" ,  "r") as ifile:
            data= ifile.read()
            dnew= data.split()
            db="".join(dnew[1:])
            passw=dnew[0]
            #print(dnew)
            mycon= sqltor.connect( host="localhost", user= "root", database='haloalkane'  , password= passw )
            if mycon.is_connected():
                print("successfully connected")
                cur=mycon.cursor()
                print('1.New purchase')
                print('2.logs')
                ent=input().lower()
                if ent=='1' or 'new' in ent:
                    proid=int(input("Enter the product id: "))
                    itnum=int(input("Enter the quantity: "))
                    ifile1=open("supply.dat","rb")
                    try:
                        d={'PRODUCT_ID':proid,'PRODUCT_NAME':''}
                        while True:
                            info=pickle.load(ifile1)
                            
                            # print(type(info))
                            # print(type(info["PRODUCT_ID"]))
                            
                            for j in info:
                                print(type(j))
                                if j['PRODUCT_ID']==proid:
                                    cost=itnum*j['PRICE']
                                    d.update(j)

                                    proid_=d['PRODUCT_ID']
                                    proname=d['PRODUCT_NAME']
                                    qut=itnum
                                    price=cost
                                    CPN= input("Enter Customer phone number :")
                                    dop=input("Enter todays date in yyyy-mm-dd format : ")
                                    
                                    mycon1= sqltor.connect( host="localhost", user= "root", database='haloalkane'  , password= passw )
                                    cur1=mycon1.cursor()
                                    
                                    l=(CPN,proid_, proname,qut,price,dop)
                                    query='insert into salenew2(CPN,PRODUCT_ID,PRODUCT_NAME,QTY,PRICE,DATE_OF_PURCHASE) values(%s,%s,%s,%s,%s,%s)'
                                    cur1.execute(query,l)
                                    mycon1.commit()
                                    print("Generating bill...........")
                                    qu= "select PRODUCT_ID , PRODUCT_NAME , QTY , PRICE, PRICE from salenew2"
                                    cur.execute(qu)
                                    res = cur.fetchall()
                                    print(res)
                                
                        
                                
                                
                                
                        
                        
                        
                    except EOFError:
                        ifile.close()

                        
                        
                        
                        
                    

