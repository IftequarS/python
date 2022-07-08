#1-convert-two-lists-into-a-dictionary
list1= ['apple', 'ball', 'cat']

list2 = [15,10,7000]
#my_dict = dict(zip(list1, list2))
my_dict = {'items' : list1, 'prize' : list2}
print("1.",my_dict)

#2: Merge two Python dictionaries into one
dict1 = {'hello' : 43110, 'ifequar' : 21, 'python' : 3.10}
dict2 = {'dictonary' : 5, 'ifequar' :21, 'lists' :4}
dict1.update(dict2)
print("2.",dict1)
dict3 = {**dict1,**dict2}
print("2.",dict3)

'''3: Print the value of key ‘history’ from the below dict
sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}'''
sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
d = sampleDict["class"]["student"]["marks"]["history"]
print("3.",d)

'''4: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}'''
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
d1 = dict.fromkeys(employees, defaults)
print("4.",d1)


'''5: Rename key of a dictionary
Write a program to rename a key city to a location in the following dictionary.
sample_dict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}'''

my_dict = {"name" : "kelly", "age" : 25,"salary": 8000,"city": "newyork"}
a1 = my_dict["location"] = my_dict.pop('city')
print("5.",my_dict)


#6.Code to find 20 is present in dict or not
dict = {'a' : 10,'b' : 20,'c' : 30}
d = dict.values()
print(d)
if 20 in d:
    print("20 is present in dict")
else:
    print("does not present")
