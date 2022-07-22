"my_file.txt" #this is name of file

Baa, baa, black sheep, have you any wool?
Yes sir, yes sir, three bags full!
One for the master,
One for the dame,
And one for the little boy
Who lives down the lane'''


#1. Write a Python program to read an entire text file.
with open("my_file.txt",'r')as entire:
    print("1.",entire.read())
    
#2. Write a Python program to read first n lines of a file.
with open("my_file.txt",'r')as f:
    file = f.readlines()
    print("2.",file)
    
'''#3. Write a Python program to append text to a file and display the text.
#with open("my_file.txt",mode="w")as app:
with open("my_file.txt",'a')as f:
    newline = f.write("\nbaa baa pink ship")
    print("my_file.txt")'''
    
#4. Write a Python program to read last n lines of a file.

#5. Write a Python program to read a file line by line and store it into a list.
#6.Write a Python program to read a file line by line store it into a variable.
#7. Write a Python program to read a file line by line store it into an array.
with open("my_file.txt",'r')as full:
    print("5.",full.readlines())
