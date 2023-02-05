#module for employee file
import pickle
import datetime as date

def newemp():

    with open("Emp.dat","ab") as ifile:
        ch=1
        while ch == 1:
            Eid= int(input("Enter emplyee id:"))
            name= input("Enter employee name:")
            dept= input("Enter dept:")
            contact= int(input("Enter the conatact number:"))
            d=date.datetime.now()
            d1= d.strftime("%y-%m-%d")
            sal= int(input("Enter salary of the enployee:"))
            data=[{'Eid':Eid , 'Ename' : name , 'Dept' : dept , 'contact': contact , 'DOH' : d1 ,'status':'active','DOR':'null', 'Salary': sal}]
            ch= int(input("Enter more rec (1- yes, 0- no) : "))
        pickle.dump(data , ifile)
    print("--------------------------------------DATA ENTERED SUCCESSFULLY-------------------------------------")


            
            
def resign(Eid):
    with open("Emp.dat" , "ab+") as updte:
        try:
            data= pickle.load(updte)
            for i in data.values():
                if Eid==data['Eid']:
                    char= input("Are you sure employee", Eid , "wants to quit??(N/Y)")
                    if char in 'Y,y':
                        data['status']= 'resigned'
                        data['DOR']= date. datetime.today()
        except EOFError:
            updte.close()
            
    print("------------------------------------------------DETAILS UPDATED------------------------------------------")
def salinc(Eid, increment):
    with open("Emp.dat" , "rb")as op:
        data= pickle.load(op)
        for i in data:
            if i['Eid']== Eid:
                i['salary']+=increment
def showemp():
    with open("Emp.dat" , "rb") as of:
        ch= 1
        while True:
            rbt= pickle.load(of)
            ch= input("Fetch more records??( 0-NO / 1- Yes )")
        print(rbt)