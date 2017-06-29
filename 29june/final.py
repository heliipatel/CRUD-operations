from connn import *
import sqlite3

def create_table():
	try:
		c.execute('''
	    CREATE TABLE users (name TEXT,
	                       phone TEXT, password TEXT)
			''')
	except Exception as e:
		print "Table is created"
con.commit()

def insert():
	name2 = raw_input("name :")
	phone2 = raw_input("phone :")
	# city2 = raw_input("city:")
	password2 = raw_input("password:")
	 
	# Insert user 1
	c.execute("INSERT INTO users(name, phone,password)VALUES(?,?,?)", (name2,phone2, password2))
	print('User inserted')
	con.commit()

def select():
	c.execute('''SELECT name, phone FROM users''')
	for row in c:
	    # row[0] returns the first column in the query (name), row[1] returns email column.
	    print('Name: {0} Phone: {1}'.format(row[0], row[1]))
	
def delete():	
	name = 'John'
	c.execute('''DELETE FROM users WHERE name = ? ''',(name,))
	print "The record which contains name=John is deleted"
	con.commit()

def update():
	name = 'Heli'
	phone = 34
	c.execute('''UPDATE users SET name = ? WHERE phone = ? ''',
	 (name,phone))
	print ("Your name is updated to Heli where phone_number = 34")