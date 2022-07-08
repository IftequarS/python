'''1.Add a list of elements to a set
Given a Python list, Write a program to add all its elements into a given set.
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]'''
sample_set = {"yellow", "orange", "black"}
sample_list = ["blue", "green", "red"]
sample_set.update(sample_list)
print('1.',sample_set)

'''2.Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
print('2.',set3)

#Write a Python program to return a new set with unique items from both sets by removing duplicates.
set4 = set1.union(set2)
print('2.',set4)

'''3. 4: Update the firstset with items that don’t exist in the second set.
Given two Python sets, write a Python program to update the first set with items that
exist only in the first set and not in the second set.
set1 = {10, 20, 30}
set2 = {20, 40, 50}'''
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print('3.',set1)

'''4.Write a Python program to remove items 10, 20, 30 from the following set at once.
set1 = {10, 20, 30, 40, 50}'''
set1 = {10, 20, 30, 40, 50}
a = set1.difference_update({10, 20, 30})
print('4.',set1)

'''5.Return a set of elements present in Set A or B, but not both.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
s = set1.symmetric_difference(set2)
print('5.',s)

'''6.Update set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}'''
set1 = {10, 20, 30, 40,50}
set2 = {30, 40, 50, 60, 70}
set2.symmetric_difference_update(set1)
print('6.',set2)

'''7.Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print('7.',set1)
