# what is Iterator
# Iterator breaks the large amount of into data tiny chunks

# How the iterator can be built
# iteration can be built based on 2 protocols
# 1. __iter__()
# 2. __next__()

# for i in range(1,5):
#     print(i)

f=["Kiwi","apple","pineapple","mango"]
"""for i in f:
    print(i)"""
i=iter(f)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
