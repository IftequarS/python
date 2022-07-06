#1.Write a Python program to sum all the items in a list.
my_list = [1,2,3,4,5,6,7]
sum_list = sum(my_list)
print(sum_list)

#2. Write a Python program to multiply all the items in a list.    
'''list = [83,8,2,12,4]
multiply_list = list.multiply()
print(multiply_list)'''

#3. Write a Python program to get the largest and the smallest number from a list.
new_list = [45,23,21,56,534]
print("The largest number in the list is ", max(new_list), "and the smallest number in the list is", min(new_list))

'''5. Write a Python program to count the number of strings where
the string length is 2 or more and the first and 
last character are same from a given list of strings.Sample List : ['abc', 'xyz', 'aba', '1221']'''
lst = ['abc', 'xyz', 'aba','1221']
length_lst = len(lst)
print(length_lst)

'''6. Write a Python program to get a list, sorted in increasing 
order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''
sample_list = [(2,5), (1, 2), (4, 4), (2, 3), (2, 1)]
s = sample_list.sort()
print(sample_list)

'''7. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']'''
new_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a = new_list.pop(0)
b = new_list.pop(3)
c = new_list.pop(3)
#poped_list = (a,b,c)
print(new_list)

#8.Write a Python program to convert a list of characters into a string.
list_char = ['i', 'f', 't', 'e', 'q', 'u', 'a', 'r']
string_char = ''.join(list_char)
print(string_char)


#9.Write a Python program to append a list to the second list.
list_1 = [12,22,32,42]
list_2 = [11,21,'least',41]
append_list = list_2.append(list_1)
#append_list = list_2 + list_1
#print(append_list)
print(list_2)

