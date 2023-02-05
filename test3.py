import salesproject
import PRODUCT
import pickle
import datetime  as date
Eid= int(input("Enter employee id :"))
with open("emp.dat" , "rb") as ofile:
    r= pickle.load(ofile)
    if r['Eid']== Eid:
        print("_______________________________________________________Wellcome_______________________________________________________")
        print("Actions to perform")
        print("1. MANAGE EMPLOYEES ")
        print("2. MANAGE STORE ")
        print("3. SELL ")
        ch= int(input("Enter choice :"))
        if ch==1:
            print("A.NEW EMPLOYEE")
            print("B. COUNT EMPLOYEES")
            print("C. RESIGN ")
            print("D. UPDATE DETAILS(salary)")
            ch2= input("ENTER CHOICE :")
            if ch2== "A" or ch2== "a":
                Eid= int(input("Enter emplyee id:"))
                name= input("Enter employee name:")
                dept= input("Enter dept:")
                contact= int(input("Enter the conatact number:"))
                d=date.datetime.now()
                d1= d.strftime("%y-%m-%d")
                sal= int(input("Enter salary of the enployee:"))
                data={'Eid':Eid , 'Ename' : name , 'Dept' : dept , 'contact': contact , 'DOH' : d1 ,'status':'active','DOR':'null', 'Salary': sal}
                salesproject.newemp(data)
            if ch2== "B" or ch2 == "b":
                pass
            if ch2== "C" or ch2 == "c":
                pass
            if ch2== "D" or ch2 == "d":
                pass
        if ch== 2:
            print("A. NEW STOCK")
            print("B. UPDATE DETAILS")
            ch3= input("ENTER CHOICE :")
            if ch3 == "A" or ch3 == "a":
                pass
            if ch3 == "B" or "b":
                pass
        if ch== 3:
            print("A . GENERATE BILL")
            print("B . SHOW DETAILS")
            ch4= input("ENTER CHOICE : ")
            if ch4 == "A" or ch4== "a":
                pass
            if ch4 == "B" or ch4 == "b":
                pass

