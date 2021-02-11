'''Write a Python program that computes the net amount of a bank account based a 
transaction log from console input. The transaction log format is shown as following: D 
100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for 
withdraw and deposit) D means deposit while W means withdrawal.
Suppose the following input is supplied to the program: 
D 300, D 300 , W 200, D 100 Then, the output should be: 500'''

import sys

balance=0.0

def deposit(balance):
	print("Your balance is : {0}".format(balance))
	dep=float(input("Enter the amount do you want deposit : "))
	balance=balance+dep
	print("After deposit the amount your balance is : {0}".format(balance))
	main(balance)

def withdraw(balance):
	print("Your balance is : {0}".format(balance))
	amount=float(input("Enter withdrawal amount : "))
	if (balance <=amount):
		print("Insufficient balance !!!")
	else:
		balance=balance-amount
		print("Bank balance is : {0}".format(balance))
	main(balance)


def main(balance):
	print('Your bank balance is : {0} '.format(balance))
	print("1) Deposit")
	print("2) Withdraw")
	print("3) Exit")
	ch=int(input("Enter your choice : "))
	if ch==1:
		deposit(balance)
	elif ch==2:
		withdraw(balance)
	elif ch==3:
		sys.exit()
	else:
		print("Please enter right choice !!!")
print('welcome to the bank')
main(0)