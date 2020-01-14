#Creating a string
s = "Hello World, how are you doing!" #Creating a string to print 
print(s)

s1 = """This is a
line of code
with multiple ines"""
print(s1)           #defining a string that contains multiple lines

print(s[0])         #indexing to find the first letter in a word using dictionaries
                    #first number in a dictionary is 0

print(s*2)          #will print it three times

print(len(s1))      #used to find the length of a string
print(len(s))

#Slicing
print(s[0:5])       #Slicing - using to find index within a string
print(s[0:])        #not closing off the index means it will splice the whole string
print(s[0:8])       
print(s[-3:-1])     #splicing using negative numbers means it indexes from the back to front

print(s[0:9:2])     #returns by skipping on variable at a time
print(s[15:: -1])   #will come from the end all the way to the beginning in reverse
print(s[::-1])      #will return the string but reversed


#Stripping
print(s.strip())    #will strip out the spaces in a string
print(s.lstrip())   #will do a left strip
print(s.rstrip())   #will do a right strip


print(s.find("ell"), 0, len(s))     #to find location of a substring. Use 0 to state where to start the search to till the length of string
print(s.count("o"))                 #counts the number of occurences of a given substring
print(s.replace("Hello", "Howdy"))  #used to replace a substring, word to get replaced goes first followed by the new word

print(s.upper)         #will return string in uppercase
print(s.lower)         #will return string in lowercase
print(s.title())       #returns a title case version of the string







