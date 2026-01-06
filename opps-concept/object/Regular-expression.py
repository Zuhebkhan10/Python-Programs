# What is regular expression:
# Regular expression is sequence of character that defines search patterns for string searching
# matching validation and manipulation

# what is module:
# A module in Python is a file that contains Python code.

# library--> packages or modules-->files
"""A library in Python is a collection of modules that are bundled together to perform related tasks.
Library = group of modules
Module = single .py file """

# Module → One chapter in a book
# Library → The full book with many chapters

import re
# Search the "Duniya" is present or not is your text
text="Welcome to the my duniya"
res=re.search("duniya",text)
print(res)
"""if "duniya" in text:
    print("present")
else:
#     print("Not present")
"""

#how many time a python has been repeated.
# findall() prints matched string in the list
player="Virat is run-machine.and Virat is my favorite player  "
res=re.findall("Virat",player)
print(res)

# replace the the zoya with duffy
# used the keyword sub()
name="Zoya is my bff. but she is very wonderful girl "
res=re.sub("Zoya","Duffy",name)
print(res)


# Split the text at each and every space
n="Call me pathan"
a=re.split(" ",n)
print(a) #Note For findall() and split() the default data type is list.


"""
cap symbols(^) --> Start with
plus(+) --> add 1 or more
Dollar-sign($) --> ends withs
Digit shorthand(\d) --> digits(0-9)
word character shorthand(\w) --> wordCharacter(a-z and A-Z ,0-9)
whitespace shorthand(\s) --> space
Asterisk(*) --> 0 or more repitations
character class[]--> set of character
Dot. --> any character expect newline
question mark ? --> 0 or 1 repitations
 """

#Extract the number from above string or check the digits in above text.
txt="the price is $99"
r=re.search(r"\$\d+",txt)
print(r)


#Extract the emails from the above list and print it in a list
t="Email: zuhebk433@gmail.com, arhamkhan898@gmail.com"
emails=re.findall(r"[a-zA-Z0-9_.]+@[a-z]+\.[a-z]+",t)
print(emails)

#validate the email
