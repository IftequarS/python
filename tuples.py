#1.Reverse the tuple
my_tuple = (12,23,34,45,56)
rev = my_tuple[::-1]
print(rev)

'''2.Access value 20 from the tuple
The given tuple is a nested tuple. write a Python program to print the value 20.
tuple1 = ('orange', [10,20,30],[5,15,25])'''
tuple1 = ('orange', [10,20,30],[5,15,25])
ind = tuple1[1][1]
print(ind)

#3.Create a tuple with single item 50.
single_tuple = (50)
print(single_tuple)

'''4.Unpack the tuple into 4 variables
Write a program to unpack the following tuple into four variables and display each variable
tuple1 = (10,20,30,40)'''
tuple1 = (10,20,30,40)
#a, b, c, d = tuple1 #this is also one method short method
a = tuple1[0]
b = tuple1[1]
c = tuple1[2]
d = tuple1[3]
print(a)
print(b)
print(c)
print(d)

# 5.Swap two tuples in Python
tpl1 = ('me', 'hi', 'hello')
tpl2 = ('you', 'hey','hry')
c = (tpl1,tpl2)=(tpl2,tpl1)
print(c)
print(tpl1)
print(tpl2)

''' 6: Copy specific elements from one tuple to a new tuple
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
tuple = (11,22,33,44,55,66)'''
tuple = (11,22,33,44,55,66)
new_tuple = tuple[3 : -1]
print(new_tuple)
