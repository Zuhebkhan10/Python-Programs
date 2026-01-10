#Except python file when we handle other files(text,json,csv,)is know
# as file handling techniques.

# open():Inbuild function to handle other files.
# there are 4-modes to handle the file.
# x, w, a, r

# 1. x-mode(execution-mode):used to create the file
# f=open("Stranger-things.txt","x")
# print(f)
# f.close()

#2. w-mode(override-mode)
# f=open("Stranger-things.txt","w")
# f.write("Welcome to the hawkings lab")
# print(f)
# f.close()

# 3.a-mode(append-mode)
f=open("Stranger-things.txt","a")
f.write(" Hello guys I'm veccna ")
print(f)
f.close()

#4. r-mode(read-mode) by-default open() is in read mode
f=open("Stranger-things.txt","r")
print(f.read())
f.close()

"""Q)can we create a new file directly by using the a & w mode
a) yes"""