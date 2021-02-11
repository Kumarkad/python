'''Write a Python program to store marks scored in subject “Fundamental of Data 
Structure” by N students in the class. Write functions to compute following:
a) The average score of class 
b) Highest score and lowest score of class 
c) Count of students who were absent for the test
d) Display mark with highest frequency
'''

import sys

def avg(marks):
	sum=0
	count=0
	for i in marks:
		sum=sum+i
		count=count+1
	average=sum/count
	print('The average score of class is : '+str(average))
	main()

def handl(marks):
	highs=max(marks)
	lows=min(marks)
	print("Highest score is : " +str(highs))
	print("Lowest score is : "+str(lows))
	main()

def countstud(marks):
	count=0
	for i in marks:
		if i <=0:
			count=count+1
	print("Count of absent student is : "+str(count))
	main()

def disp(marks):
	marks.sort()
	print("Display marks with high frequency is : ")
	for i in marks:
		print(i)
	main()

def main():
#	marks=[35,40,12,99,67,32,76,0,10,56,65,91,45,39]
	marks=[]
	num=int(input("Enter the no. of entry : "))
	print("Enter the marks : ")
	for i in range(num):
		element=int(input())
		marks.append(element)
	print("1) The average score of class")
	print("2) Highest score and lowest score of class")
	print("3) Count of students who were absent for test")
	print("4) Display marks with high frequency")
	print("5) Exit")
	ch=int(input("Enter your choice : "))
	if ch==1:
		avg(marks)
	elif ch==2:
		handl(marks)
	elif ch==3:
		countstud(marks)
	elif ch==4:
		disp(marks)
	elif ch==5:
		sys.exit()
	else:
		print("Please enter right choice !!!")

main()