# https://www.geeksforgeeks.org/python-launch-a-web-browser-using-webbrowser-module/

import webbrowser
import requests
# r = requests

# -- here is how to open an URL using webbrowser module
# print(webbrowser.open('http://www.cityu.edu'))
# -- now we can extract some content/text from the webpage
print(webbrowser.open('https://w3schools.com/python/'))
print(webbrowser.open('https://w3schools.com/python/demopage.htm'))


# The Hypertext Transfer Protocol (HTTP) is designed to enable communications between clients and servers.
# HTTP works as a request-response protocol between a client and server.
# Example: A client (browser) sends an HTTP request to the server; then the server returns a response to the client. The response contains status information about the request and may also contain the requested content.
# HTTP Methods
# GET
# POST
# PUT
# HEAD
# DELETE
# PATCH
# The GET Method
# ----------------
# GET is used to request data from a specified resource.
# GET is one of the most common HTTP methods.
# Note that the query string (name/value pairs) is sent in the URL of a GET request:
# /test/demo_form.php?name1=value1&name2=value2
# = cached, stays in the browser history
# The POST Method 
# ----------------
# POST is used to send data to a server to create/update a resource, for instance, user=, password
# The data sent to the server with POST is stored in the request body of the HTTP request:
# = not cached, doesn't persiste in the browser
# -- getting the html property
res = requests.get('https://w3schools.com/python/demopage.htm') 
print(res.content) # content writting in bytes
print(res.text) # content writting in unicode UTF-8

# -- getting the json property
res = requests.get('https://www.w3schools.com/python/demopage.js')
print(res.json())

# -- let's try to make a request of an image, then store it into content attribute and finally save it to our disk.
webbrowser.open_new("")
robj = requests.get("https://www.python.org/static/img/python-logo.png")
with open("c:\\temp\\python.png", 'wb') as fp:
    fp.write(robj.content)

# -- There are several different methods in HTTP connection, GET, POST
# When HTTP is used, as is most common, the operations (HTTP methods) available are GET, HEAD, POST, PUT, PATCH, DELETE, CONNECT, OPTIONS and TRACE.
# request the text of the webpage
url = 'https://httpbin.org/get'
robj = requests.get(url)
print(robj.text)

#
# -- now let's create a url with query string GET defined in dictionary, key=value pair
#
url1 = 'https://www.tennis-warehouse.com/searchresults.html'
payload = {'search': 'products', 'searchtext': 'prince'}

robj = requests.get(url1, params=payload) # payload = url parameter set
#https://www.tennis-warehouse.com/searchresults.html?search=products&searchtext=head&opt_page=1&opt_sort=alphaAtoZ
# https://en.wikipedia.org/wiki/Query_string
# The series of pairs is separated by the ampersand
webbrowser.open_new(robj.url)
print(robj.url)
print(robj.headers)
print(robj.content)
print(robj.text)
print(dir(robj))
print("status = " + str(robj.status_code)) # 200 = Success, 400 = Not Found, 500 = Server not responding
if(robj.status_code == 200):
    print("Success")
else:
    print("Not Found!")
print(robj.ok)


# -- here is the POST request and let's see what it does
# POST request puts those payload dictionary data into a form expecting the 
# HTTP will upload or update the display according to the data provided into the form key:value pair.
# check the URL and it doesn't have the payload information but shows up in the field of form.
url = 'https://httpbin.org/post'

payload = {"username": "Jin", "password": "hello123", "platform": "Windows"}
robj = requests.post(url, data=payload) # payload = url parameter set
print(robj.text)
print(robj.json()) # essentially returns the dictionary format of the contents
robj_dict = robj.json()
print(robj_dict["url"])
print(robj_dict["form"])
print(robj_dict["origin"])


# Posting to a website.
url = 'https://jsonplaceholder.typicode.com/posts'

data = {'title':'Python Requests Post Testing','body':'I love Python','userId':'jin.chang@gmail.com'}
response = requests.post(url, data) 
print(response.status_code) 
print(response.text) 


# OPTIONAL
# -- one more example of authentication using get on the httpbin.org's Auth parameter
# document for auth in requests = https://requests.readthedocs.io/en/master/user/authentication/
# requests.get('https://api.github.com/user', auth=('user', 'pass'))
# <Response [200]>

# first go to https://httpbin.org/ and under Auth, register with user id and password
url = "https://httpbin.org/basic-auth/Jin/hello12"
robj = requests.get(url, auth=('Jin', 'hello12'))
print(robj.text)
print(robj.status_code) # 200 = Success, 401 = Unsuccessful



url = 'https://jsonplaceholder.typicode.com/todos/1'
# The status code 200 means a successful execution of request and response.content will return the actual JSON response of a TODO item.
print(robj.status_code) 
robj = requests.get(url)
print(robj.text)



