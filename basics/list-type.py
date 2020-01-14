#Creating Lists
lst = [10,20, 'Nico', -10, 30.5]        #defining the list - any type of data type can be added
print(lst)
print(lst[3])                          #returns the 4th variable in the list      
print(lst[3:5])                        #performing slicing on the list
print(lst*4)                           #returns string four times
print(len(lst))                        #find length of list


lst.append(40)                         #.append used to add to the list
lst.remove('Nico')                     #.remove used to remove values from the list
del(lst[1])                            #to delete values using index
print(lst)



print(max(lst))                        #to print maximum element in list
print(min(lst))                        #to print minimum element in list

lst.insert(3, 99)                      #to insert a new value to list
print(lst)

lst.sort(reverse = True)               #used to sort the list a different wauy
print(lst)