import sys

a=['rocky','raj','akash','shubham','kumar','suraj','manoj','sid']
b=['siraj','manasi','kriti','kiran','kumar','akash','rocky']
c=['virat','suresh','ravindra','sunil','sid','akshay','shubham','siraj']
d=[]

def cb():
	for i in a:
		if i in b:
			d.append(i)
	print("List of students who play both cricket and badminton : ")
	for p in d:
		print(p)
	main()
	
def cab():
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
	for i in c:
		if i not in a and i not in b:
			d.append(i)
	print(" List of students who play neither cricket nor badminton :")
	for p in d:
		print(p)
	main()
	
def cf():
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