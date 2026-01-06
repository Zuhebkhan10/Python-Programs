# Map(): map function takes a function as an argument and run over each element in the collection.
# Syntax :collection_type(map(func,col_name))

#print the of each item in a new list.

f=["Kiwi","Banana","pineapple","Orange"]
m=list(map(len,f))
print(m) #(length of each element)

# using normal function
player=["Virat","Zuheb","Jitesh","Salt","Livingstong","Rinku"]
n=[]
for i in player:
    n.append(len(i))
print(n)


#Using the list-comprehension
hero=["Salman","Amir","Mahes-babu"]
n=[len(i) for i in hero]
print(n)

#Convert the list of string number into list integers
user=input("Enter a number").split()
# print(user)
for i in user:
    #print(i)1
    #print(type(i))
    #print(int(i))
    c=tuple(map(int,user))
    #print(c)
#print(type(c))

# Note: When there is more user input we use the map()

#lambda function for using even or odd
n=[1,2,3,42,11,45,12,18]
res=list(map(lambda num: num%2==0,n))
print(res) # the output is True(even) and False(odd) format



#filter():- take a function as an argument and run over each element in collection and print the data which is condition true.
num=[10,20,304,40,55,60]
f1 = list(filter(lambda res: res%2==0,num))
print(f1)