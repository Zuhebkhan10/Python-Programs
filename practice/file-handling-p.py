# x-mode
# f=open("Got.txt","x")
# print(f)
# f.close()

# w-mode
f=open("Got.txt","w")
f.write("Winter is coming and are you ready start the war for stark and tarageryn houses. \n")
print(f)
f.close()

# append-mode
f=open("Got.txt","a")
f.write("This is john snow and his sister name is arya stark")
print(f)
f.close()


# read-mode
f=open("Got.txt","r")
print(f.read())
f.close()


# Pickling-file
import pickle

data=[10,20,30,"Zuheb","Suhail","Fahad"]

with open("data.pkl","wb")as f:
    pickle.dump(data,f)
print("Data successfully recievd ")


with open("data.pkl","rb")as f:
    data=pickle.load(f)
    print(data)