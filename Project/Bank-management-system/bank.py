import sqlite3

conn=sqlite3.connect('bank.db')
query=conn.cursor()

query.execute("create table if not exists customer(id integer PRIMARY KEY ,name text,mobile_no integer,email text, password text, account_type text,balance real)")

entity=(1,'kumar',7875185100,'kumarkad03@gmail.com','Kumar@03','saving',10000)
query.execute('insert into customer(id,name,mobile_no,email,password,account_type,balance) values (?,?,?,?,?,?,?)',entity)

query.execute('select * from customer')
rows=query.fetchall()
for row in rows:
	print(row)

conn.commit()