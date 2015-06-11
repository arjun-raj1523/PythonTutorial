#!C:/Python/python.exe

import cgi
import json
import urllib2
from pprint import pprint
import urllib, json

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


#def getData():
#	formData = cgi.FieldStorage()
#	firstName = formData.getvalue('firstName')
#	lastName = formData.getvalue('lastName')
#	return firstName,lastName
	
def getData_DiffFormat():
	formData = cgi.FieldStorage()
	firstName = formData.getvalue('firstName')
	lastName = formData.getvalue('lastName')
	lat = formData.getvalue('lat')
	lng = formData.getvalue('lng')
	resultSet = {'firstName':firstName , 'lastName':lastName}
	return lat,lng

def getJSON():
	
	url = "https://api.foursquare.com/v2/venues/search?ll=40.7,-74&limit=5&oauth_token=QBYJF4RXJRYJNYEHWQDHAX54D04ORLKEVKPDTFTSYIUJZXPW&v=20150603"
	response = urllib.urlopen(url);
	data1 = json.loads(response.read())	
	data2 = data1['response'] 
	print('<ol>')
	for x in range(0,5):
		print('<li>')
		print data2['venues'][x]['name'],','
		print('</li>')
	print('</ol>')

#main Program

if __name__== "__main__":
	try:
		htmlTop()
		result=getData_DiffFormat()
		print result
		htmlTail()
	except:
		cgi.print_exception()
