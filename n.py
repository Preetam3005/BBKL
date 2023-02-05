import pickle
with open("supply.dat" , "rb") as ofile:
    data= pickle.load(ofile)
    print(data)
