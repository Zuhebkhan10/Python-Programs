# #configure the current running file in the pycharm -->
# #fn + shift + cntrl + f10
#
# #ARGS
# #Kwargs
# #Return
# #test-case --> fibonacci series, prime number detection , pattern
#
# #parameters :- when we define a function we create variable
# #argument:- when we call a function we pass some values
# #Default functions:- when we define a function we create a variable(parameter) and by default we assign a value
# #29-12-2025
# #what we need to do when we dont know how many parameters we need to pass?
# def details(**name):
#     print(name)
# #details(name="shahul",gender="male",mobile=93783783)
# #what we need to do when we dont know how many arguments we need to pass?
# #print the sum of all the given numbers --> 1,2,3,4,5,6,7,8,9
# """def sum(*n1):
# print(n1)
#
# sum(1,2,3,4,5,6,7,8,9,10)"""
#
# """
# ** --> KWARGS --> keyword arbitrary arguments
# --> when we dont know how many parameters we need to pass we use kwargs
# --> The default data type for kwargs is dictionary
# * --> ARGS --> Arbitrary Arguments
# -->when we dont know how many arguments we need to pass we use args
# --> The default data type for args is tuple"""
#
# #create a sum function
# t = (1,2,3,4,5,6,7,8,9)
# #print(sum(t))
# total = 0
# for i in t:
#     #print(i)
# total = total + i
# #print(total)
# #
# def sum(*num):
#     total = 0
# for i in num:
#     total = total + i
# print(total)
# #sum(1,2,3,4,5,6,7,8,9,10,29,35)
#
# #sum(10,20,30,40,50,60,70,80,90)
#
# # Return: keyword send back all the values to the caller
# # return is similar to print(), when we use the return call the function with print()
#
# def sum(*num):
# total = 0
# for i in num:
# total = total + i
# return(total)
#
# #print(sum(1,2,3,4,5))
# #write a function that returns the greater number from 2 numbers
# #10,15
# """a = 10
# b = 15
# if a > b:
# print(a)
# else:
# print(b)"""
# def maximum(a,b):
# if a>b:
#     return a
# else:
# return b
# #print(maximum(a,b))
#
# #create a function to print the length of a string
# #len()
# #write a function to calculate the factorial of a number --> 5*4*3*2*1
#
# #range(s,e,st):- to generate range of numbers in for loop
# """fact = 1
# for i in range(1,11):
# fact = fact*i
# print(fact)"""
# def factorial(n,m):
# fact = 1
# for i in range(n,m+1):
# fact = fact*i
# return fact
# print(factorial(1,5))
#
# #what is function?
# #How can we create a function --> def
# #what is a parameter(variable) and arguments(values)?
# #what is default function?(by default assign a value to parameter)
# #what is args and kwargs?
# #what is the default data types for ARGS and KWARGS?
# #What is return keyword?
# #How many arguments and parameters can we create?
# ​
