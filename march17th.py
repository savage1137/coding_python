# create and print a list
a=[]
for i in range(11):
    a.append(i)
print(a)

# access element in the list and modify the list
b=a.index(3)
print(b)
a[b]=300
print(a)

# remove
a.pop(2)
print(a) 

# copy using slicing
a[0:]
print(a)

# copy using constructor
b = list(a)
print(b)