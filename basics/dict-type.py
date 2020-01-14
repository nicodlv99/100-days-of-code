dict1 = {1: "john", 2: "bob", 3: "bill"}    #the numbers are the keys (ID) and the value is the name
print(dict1)

print(dict1.items())

k = dict1.keys()                            #used to find the keys in a dictionary
for i in k:print(i)

v = dict1.values()                          #used to find the values in a dictionary
for i in v: print(i)

print(dict1[3])                             #will print the third value in the dictionary

del dict1[2]                                #used to delete values from the dictionary
print(dict1)
