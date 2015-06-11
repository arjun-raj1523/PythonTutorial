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


def connectDB():
        #Connect to DB
        db = conn.connect(host= 'localhost', user='root',passwd='')
        cursor =db.cursor()
        return db,cursor

def fetchData(db,cursor):
        #insert Data into DB
        sql = 'use exampledb'
        cursor.execute(sql)
        sql="select * from person"
        cursor.execute(sql)
        people = cursor.fetchall()
        return people

def displayData(people):
        #display Data
        print('''<table>
                <tr>
                <th>ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                </tr>''')
        for x in people:
                print("<tr>")
                print("<td>{0}</td>".format(x[0]))
                print("<td>{0}</td>".format(x[1]))
                print("<td>{0}</td>".format(x[2]))
                print("</tr>")
        print("</table>")


#main Program

if __name__== "__main__":
	try:
		htmlTop()
		db,cursor = connectDB()
		people = fetchData(db,cursor)
		cursor.close()
		displayData(people)				
		htmlTail()
	except:
		cgi.print_exception()
