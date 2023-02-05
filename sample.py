import pickle
with open("Emp.dat" , "rb") as of:
    of.seek(0)
    ch= 1
    while True:
        rbt= pickle.load(of)
        ch= input("Fetch more records??( 0-NO / 1- Yes )")
        print(rbt)