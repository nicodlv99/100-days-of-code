s = {10, 20, 30, "XYZ", 10, 20, 10}     #defining the set - does not allow duplicates
print(s)
print(type(s))

s.update([88, 99])
print(s)
print(type(s))

#sets do not allow duplicates or allow the following operations: indexing,slicing or repetition

f = frozenset(s)
f.remove(20)