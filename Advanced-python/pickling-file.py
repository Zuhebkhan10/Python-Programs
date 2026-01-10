# Pickling-data: pickling is the process of converting a python objects into bytes
# stream ad saving it to a file

# The process of serialization and deserialization is known as pickling.

import pickle
data=[10,20,304,500]

#pickle-file(Serialization)
# with open("data.pkl","wb")as f:
#     pickle.dump(data,f)
# print("data pickled successfully ")

# unpickle-file(deserialization)
with open("data.pkl","rb") as f:
    data=pickle.load(f)
    print(data)