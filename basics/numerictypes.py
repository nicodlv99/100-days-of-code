#Integer types
a = 13 #assigning value to a variable
b = 100
c = -66
print(a, b, c)  #printing the value of the variable
print(type(a)) #used to find the type of variable that 'a' is

#Floating point types
x = 33.5
y = -25.8
z = 205
print(x , y, z)
print(type(z))

#Defined complex types
d = 3+5j
print(d)
print(type(d))

#Binary types
e = 0B1010 #binary literal value starts with 0B
print(e) #print decimal value of the binary value 

#Hexadecimal types
f = 0XFF #when FF is converted from hexadecimal point converts to 255
print(f)
print(type(f))

#Boolean 
g = True #Use bool in conditions and looping statements to define conditions within programs
print(g) 
print(type(g))
print(9>8) #returns bool True 

#Type conversion functions
h = int(x) #used to convert the float type (33.5) to an integer 
print(h)
print(type(h))

i = float("22.5") #converts string to float
print(i)
print(type(i))



