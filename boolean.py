#1.Take two inputs from user and check whether they are equal or not.
user_no1 = int(input("Enter any number\n"))
user_no2 = int(input("Enter any number\n"))
boolean = user_no1==user_no2
print("The given inputs are:-",boolean)


'''2.Take 3 inputs from user and check :
all are equal
any of two are equal
( use and or )'''
one = int(input("Enter no. one \n"))
two = int(input("Enter no. two \n"))
three = int(input("Enter no. three \n"))
#print(one, two, three)
all_equal = one==two and two==three and three==one
print("all are equal:-",all_equal)
'\n'
any_two_equal = one==two or two==three or three==one
print("any two are equal:-",any_two_equal)


#3.Take two number and check whether the sum is greater than 5, less than 5 or equal to 5.
num1 = int(input("Enter a number1\n"))
num2 = int(input("Enter a number2\n"))
num3 = num1+num2
print("The sum is greater than 5",num3>5)

print("The sum is less than 5",num3<5)

print("The sum is equal to 5",num3==5)

'''4.Judge the follwing expressions :
not(True and True)
True or False
not(False and True)
False and False'''
print(not(True and True))
print(True or False)
print(not(False and True))
print(False and False)

'''5.Suppose passing marks of a subject is 35. Take input of marks from user
and check whether it is greater than passing marks or not.'''
marks = int(input("Enter marks obtain:"))
passing_marks = 35
print("The marks obtain is more than 35:",marks>35)
#print("The marks obtain is less than 35:",marks<35)
#print("The marks obtain is equal to 35:",marks==35)
