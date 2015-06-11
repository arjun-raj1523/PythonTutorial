#!/usr/bin/python

import cgi

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

#main Program

if __name__== "__main__":
	try:
		htmlTop()
		print("Hello World!")
		htmlTail()
	except:
		cgi.print_exception()