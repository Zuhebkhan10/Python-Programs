#List comprehension : It offers smaller line of code where a new list is created from the existing list
f=["apple","pineapple","banana","kiwi"]
new=[]
for i in f:
    if "e" in i:
        new.append(i)
print(new)


# Syntax LC
#[Items for item i collection_name <space> if condition]
new1=[i for i in f if "a" in i]
print(new1)


#Seprate  the even number in a new list by using LC
l=[12,32,12,44,31,91,97,73]
new=[i for i in l if i%2==0]
print(new)

#print the square of even number  in above list
new3=[i**2 for i in  l if i%2==0]
print(new3)

# print the fruits in uppercase
u=[i.upper() for i in f]
print(u)