lst = [20, 30, 40, 234]     
print(type(lst))
b = bytes(lst)              #to convert the list into bytes
print(type(b))              #shows type bytes


b1 = bytearray(lst)         #converting list into a bytes array
print(type(b1))
b1[2] = 33                  #a byte array can be assigned values through indexing

#no slicing or repetition allwoed on bytes or bytes array