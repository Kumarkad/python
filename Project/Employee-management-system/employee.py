import sqlite3
import sys
from prettytable import PrettyTable

table=PrettyTable(['Id','Employee Name','Salary','Dept','Position','HireDate'])

conn=sqlite3.connect('emp.db')
query=conn.cursor()
query.execute("create table if not exists employees(id integer PRIMARY KEY,name text,salary real,department text,position text,hireDate text)")

def add_record():
	id=int(input('Enter the Employee id : '))
	name=input('Enter the Employee name : ')
	salary=float(input('Enter the Employee salary : '))
	dept=(input('Enter the Employee department : '))
	position=(input('Enter the position of Employee : '))
	hiredate=(input('Enter the hiredate of Employee : '))
	entity=(id,name,salary,dept,position,hiredate)
	
	query.execute('insert into employees (id,name,salary,department,position,hiredate) values (?,?,?,?,?,?)',entity)
	print('Record successfully inserted !!!')
	conn.commit()
	menu()

def search_record():
	a=int(input("Enter the Employee id to search : "))
	query.execute('select * from employees where id=?',(a,))
	rows=query.fetchall()
	for row in rows:
		print(row)
	menu()
	
def dept_search():
	a=input("Enter the Department to display Employees : ")
	query.execute('select * from employees where department=?',(a,))
	rows=query.fetchall()
	for row in rows:
		print(row)
	menu()

def display_record():
	query.execute('select * from employees')
	table.clear_rows()
	rows=query.fetchall()
	for row in rows:
		table.add_row(row)
	print(table)
	menu()

def update_record():
	a=input("Enter the Employee id to update the employee information : ")
	name=input('Enter the Employee name : ')
	salary=float(input('Enter the Employee salary : '))
	dept=(input('Enter the Employee department : '))
	pos=(input('Enter the position of Employee : '))
	hdate=(input('Enter the hiredate of Employee : '))
	query.execute('update employees set name=?,salary=?,department=?,position=?,hireDate=? where id=?',(name,salary,dept,pos,hdate,a,))
	print('Record updated successfully !!!')
	conn.commit()
	menu()

def delete_record():
	a=input("Enter the Employee id to delete the Employee : ")
	query.execute('delete from employees where id=?',(a,))
	print(query)
	conn.commit()
	menu()

def exit():
	print("Createt by \U0001F449 Kumarkad03_KD\U0001F60E")
	sys.exit('\U0001F64F \U0001F64F \U0001F64F Thank you for using Employee management system \U0001F64F \U0001F64F \U0001F64F ')

def menu():
	print('\nEMPLOYEE MANAGEMENT SYSTEM')
	print('\n\U0001F916 \U0001F468 \U0001F4BB \U0001F6E0 \U0001F4BC  \U0001F527 \U0001F5A5  \U0001F468 \U0001F916')
	print("\nEnter Your Option : \n")
	print("1"+"\U0001F449"+"Add a new record")
	print("2"+"\U0001F449"+'Search record from employee id')
	print('3'+'\U0001F449'+'List of employee from particular department')
	print('4'+'\U0001F449'+'Display all employee')
	print('5'+'\U0001F449'+'Update record of an employee')
	print('6'+'\U0001F449'+'Delete record of an employee')
	print("7"+"\U0001F449"+'Exit\n')
	choice=int(input('Enter your choice : '))
	
	if choice==1:
		add_record()
	elif choice==2:
		search_record()
	elif choice==3:
		dept_search()
	elif choice==4:
		display_record()
	elif choice==5:
		update_record()
	elif choice==6:
		delete_record()
	elif choice==7:
		exit()
	else:
		print("Please enter right option !!!")

print("\U0001F490\U0001F490\U0001F490"+"   Welcome    "+"\U0001F490\U0001F490\U0001F490")

menu()
conn.commit()