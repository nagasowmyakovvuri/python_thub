##a=open('sowmya.txt','x')  creating a new file
##a.close()
##a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\file handling in pyhton\sowmya123.txt','x')
##a.close()


##a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\file handling in pyhton\sowmya123.py','x')

##a.close()
##a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\file handling in pyhton\sowmya123.txt','w')
##a.write("hi! how are you\n")  w-->writing in a file
##a.write("welcome to my world")##old content will be updated by the new content and old content will be removed
##a.close()

##a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\file handling in pyhton\sowmya1263.txt','w')
##a.write("arjun is the supreme hero")##if the file is not there also w will create and push the content.
##a.close()

##in order to save the information in the file we use append mode for writing an additional information
##and also creates the new file

##a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\file handling in pyhton\sowmya123.txt','a')
##
##a.write("save your time by using it for right purposes")##old content will be updated by the new content and old content will be removed
##a.close()
 #inorder to read the content in the file we use read mode
##a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\file handling in pyhton\sowmya123.txt','r')
####c=a.read()
##f=a.readlines()
####print(c)
##for i in f:
##    print(i)
##a.close()


##inorder to delete a file we use os module
##import os
##os.remove(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\file handling in pyhton\sowmya123.py')

## to make  a folder
##import os
##os.mkdir(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\xyz\abc')
##import os
##os.rmdir(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\xyz')

##csv-->comma separated value same as excel sheet
#task-->on cars
##a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\text and word documents\cars.csv','r')
####c=a.read()
##f=a.readlines()
##for i in f:
##    print(i)
##a.close()

##a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\text and word documents\cars.csv','r')
##b=[]
##c=a.readlines()
##for i in c:
##    i=i.split(",")
##    b.append(i)
##a.close()

##a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\text and word documents\cars.csv','r')
##b=[]
##c=a.readlines()
##for i in c:
##    i=i.split(",")
##    b.append(i)
##a.close()
##for i in b:
##    print(i[-1])


##r+-->read,write
##w+-->write,read
##a+-->write,read


##with open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\text and word documents\cars.csv','r') as a:
##      b=[]
##      c=a.readlines()
##      for i in c:
##           i=i.split(",")
##           b.append(i)
##      a.close()
##      for i in b:
##          print(i[-1])
##
##import csv
##b=[]
####with open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\text and word documents\cars.csv','r') as a:
##    
####      data=csv.reader(a)
##    data=list(csv.reader(a))

##a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\file handling in pyhton\sample123.txt','a')
##a.write("hi\n")
##a.write("this is sowmya")
##a.close()

##l=["hi this is sowmya\n","kovvuri\n","naga\n"]
##a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\file handling in pyhton\sample123.txt','w')
##for i in l:
##    a.write(i)
##a.close()

l=["hi this is sowmya\n","kovvuri\n","naga\n"]
a=open(r'C:\Users\nagas.LAPTOP-K2LUQ01O\OneDrive\Documents\file handling in pyhton\sample123.txt','w')
a.writelines(l)
a.close()

































































