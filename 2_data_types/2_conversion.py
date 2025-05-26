# implicit type conversion
# bool -> int -> float -> complex


#explicit type conversion
print(int(10.3)) # output : 10
print(float(10)) # output : 10.0
print(str(10.3)) # output : 10.3
# for bool : false if 0, 0.0, '', [], None : else true
print(bool(10.3)) # output : true

# below can be used only with iterable object
# print(list(10.3)) # TypeError: 'float' object is not iterable
print(list("nk"))
print(tuple("nk"))
print(set("nk"))


# common method for dictionary conversion
keys = [1,2,3]
values = [4,5,6]
print(dict(zip(keys,values)))