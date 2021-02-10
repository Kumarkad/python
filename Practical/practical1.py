"""In second year computer engineering class, group A student’s play cricket, group B 
students play badminton and group C students play football. 
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton 
b) List of students who play either cricket or badminton but not both 
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET 
built-in functions) """

import sys

a=['rocky','raj','akash','shubham','kumar','suraj','manoj','sid']
b=['siraj','manasi','kriti','kiran','kumar','akash','rocky']
c=['virat','suresh','ravindra','sunil','sid','akshay','shubham','siraj']


def cb():
	d=[]
	for i in a:
		if i in b:
			d.append(i)
	print("List of students who play both cricket and badminton : ")
	for p in d:
		print(p)
	main()
	
def cab():
	d=[]
	for i in a:
		if i not in b:
			d.append(i)
	for i in b:
		if i not in a:
			d.append(i)
	print("List of students who play either cricket or badminton but not both : ")
	for p in d:
		print(p)
	main()
	
def ncb():
	d=[]
	for i in c:
		if i not in a and i not in b:
			d.append(i)
	print(" List of students who play neither cricket nor badminton :")
	for p in d:
		print(p)
	main()
	
def cf():
	d=[]
	for i in a:
		if i not in b:
			d.append(i)
	for i in c:
		if i not in b and i not in d:
			d.append(i)
	print("Number of students who play cricket and football but not badminton : ")
	for p in d:
		print(p)
	main()

def main():
	print(" 1) List of students who play both cricket and badminton ")	
	print(" 2) List of students who play either cricket or badminton but not both ")
	print("3) List of students who play neither cricket nor badminton")
	print("4) Number of students who play cricket and football but not badminton")
	print("5) Exit")
	
	ch=int(input("Enter your choice : "))
	if(ch==1):
		cb()
	elif(ch==2):
		cab()
	elif(ch==3):
		ncb()
	elif(ch==4):
		cf()
	elif(ch==5):
		sys.exit()
	else:
		print("Please enter right choice !!!")
		main()

main()