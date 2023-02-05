#module for stock and resources
import pickle 
def newstock(data):
    with open("supply.dat","ab") as ofile:
        pId= int(input("Enter product id:"))
        Prdct= input("Enter the name of the product:")
        brnd= input("Enter company of manufacturing:")
        stock= int(input("Enter the total stock to be input:"))
        if stock >= 1:
            availability= 'IN STOCK'
        else:
            availability= 'OUT OF STOCK'
        prc= int(input("enter the price of the item:"))
        data={PRODUCT_ID: pId , PRODUCT_NAME: Prdct,COMPANY: brnd ,AVAILABILITY:availability,PRICE:prc}
        pickle.dump(data,ofile)
        print("-----------------------------------------------DATA ENTERED SUCCESSFULLY------------------------------------------")

def add(PRODUCT_ID,STOCK=1):
    with open("supply.dat", "rb+") as ifile:
        d= pickle.load(ifile)
        for i in d:
            if i[PRODUCT_ID]== PRODUCT_ID:
                i[STOCK]+=STOCK


def sold(PRODUCT_ID,nos):
    with open("supply.dat","rb+") as opd:
        D= pickle.load(opd)
        for i in D:
            if i[PRODUCT_ID]==PRODUCT_ID:
                i[STOCK]-= nos

