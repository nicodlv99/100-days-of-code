tpl = (40, 50, 40, "XYZ")       #defining the tup;e
print(tpl)
print(tpl[3])                   #used to find third value of tuple
print(tpl*3)
print(tpl.count(40))            #used to find how many times a value occurs in a tuple
print(tpl.index("XYZ"))         #used to find the index of a value in a tuple

lst = [67, 34, "XYZ"]
print(type(lst))
tpl1 = tuple(lst)               #converting the list into a tuple
print(type(tpl1))
