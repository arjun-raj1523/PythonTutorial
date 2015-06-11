#!C:/Python/python.exe

import cgi
import mysql.connector as conn

def htmlTop():
	print("""Content-type:text/html\n\n
			 <html>
			 	<head>
			 		<title>Python</title>
			 	</head>
			 	<body>""")

def htmlTail():
	print("""</body>
				</html>""")


def getData():
        #get Data from from
	formData = cgi.FieldStorage()
	firstName = formData.getvalue('firstName')
	lastName = formData.getvalue('lastName')
	return firstName,lastName

def connectDB():
        #Connect to DB
        db = conn.connect(host= 'localhost', user='root',passwd='')
        cursor =db.cursor()
        return db,cursor

def createDB(db,cursor):
        #create DB
        sql = 'create database exampledb'
        cursor.execute(sql)
        db.commit()
        
def createEntity(db,cursor):
        sql = 'use exampledb'
        cursor.execute(sql)
        sql='''create table person
               (personid int not null auto_increment,
                firstname varchar(20) not null,
                lastname varchar(20) not null,
                primary key(personid))'''
        cursor.execute(sql)
        db.commit()

#main Program

if __name__== "__main__":
	try:
		htmlTop()
		result = getData()
		db,cursor = connectDB()
		createDB(db,cursor)
		createEntity(db,cursor)
		cursor.close()
		htmlTail()
	except:
		cgi.print_exception()
