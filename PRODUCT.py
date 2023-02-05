#module for stock and resources
import salesproject
import pickle 
def newstock():
    with open("supply.dat","ab+") as ofile:
        ch=1
        while ch==1:
            pId= int(input("Enter product id:"))
            Prdct= input("Enter the name of the product:")
            brnd= input("Enter company of manufacturing:")
            stock= int(input("Enter the total stock to be input:"))
            if stock >= 1:
                availability= 'IN STOCK'
            else:
                availability= 'OUT OF STOCK'
            prc= float(input("enter the price of the item:"))
            
            data=[{"PRODUCT_ID": pId , "PRODUCT_NAME": Prdct ,"COMPANY": brnd ,"AVAILABILITY":availability,"PRICE":prc,'STOCK':stock}]
            
            ch= int(input("Do you want to enter more records : (1- yes/ 0- NO)"))
        
            pickle.dump(data,ofile)
        print("Thank You")
        print("-----------------------------------------------DATA ENTERED SUCCESSFULLY------------------------------------------")

def add(PRODUCT_ID,STOCK=1):
    x=open('supply.dat','rb')
    try:
        d= pickle.load(x)
        print(type(d))
        for i in d:
           
            if i["PRODUCT_ID"]== PRODUCT_ID:
                i["STOCK"]+=STOCK
                print("Data added succesfully..")
    except EOFError:
        x.close()
def incprc(PRODUCT_ID , INC):
    with open("supply.dat", "rb+") as zfile:
        og= pickle.load(zfile)
        for i in og:
            if i["PRODUCT_ID"] == PRODUCT_ID:
                i["PRICE"]+=INC
        print("-----------------------------------------------Data updated-----------------------------------------------")
def Decprc(PRODUCT_ID, DEC):
    with open("supply.dat" , "rb+") as afile:
        dc= pickle.load(afile)
        for i in dc:
            if i["PRODUCT_ID"]== PRODUCT_ID:
                i["PRICE"]-= DEC
        print("-----------------------------------------------Data updated-----------------------------------------------")
def sold(PRODUCT_ID,nos):
    with open("supply.dat","rb+") as opd:
        D= pickle.load(opd)
        for i in D:
            if i["PRODUCT_ID"]==PRODUCT_ID:
                i["STOCK"]-= nos
def showstock():
    with open("supply.dat" ,"rb") as ifle:
        rbt= pickle.load(ifle)
        print(rbt)

