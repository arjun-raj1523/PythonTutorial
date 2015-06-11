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

def insertData(db,cursor):
        #insert Data into DB
        firstName,lastName = getData()
        sql = 'use exampledb'
        cursor.execute(sql)
        sql="INSERT INTO `person`(`firstname`, `lastname`) VALUES ('%s','%s')" %(firstName,lastName)
        cursor.execute(sql)
        db.commit()  

#main Program

if __name__== "__main__":
	try:
		htmlTop()
		db,cursor = connectDB()
		insertData(db,cursor)
		print "<h1>Insertion Done</h1>"
		cursor.close()
		htmlTail()
	except:
		cgi.print_exception()
