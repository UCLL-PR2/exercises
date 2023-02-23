# Exercise Serialization/deserialization using Flask

This exercise uses the Flask web framework, which makes it easy to build and deploy web applications in Python. To complete this exercise, you will need to install Flask by running the following command:

```python
pip install flask
```

- In the server.py file in the server map we first need to import the Flask class. An instance of this class will be our WSGI (Web Server Gateway Interface) application.

- Next we create an instance of this class. The first argument is the name of the application’s module or package. \_\_name\_\_ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

- We then use the route() decorator to tell Flask what URL should trigger our function.

- The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```
To start the server, run the following command:

```python
python server.py
```
You can then send requests to the server by visiting http://localhost:5000 in a web browser. This simple example only handles a single endpoint (/), but you can add more endpoints by using the @app.route decorator. For example:

```python
@app.route('/users/<username>')
def show_user(username):
    return f'User: {username}'
```
If you vist http://localhost:5000/users/jef then your should see the **jef**. Instead of visiting the website we want to send the requests in our client.py file. We can do that as follow:

```python
import requests #pip install requests

#The GET method is used to access data for a specific resource
res = requests.get('http://localhost:5000/users/jef')
if res.ok:
    print(res.text) ## Return a string representation of the data payload
```

You can run this code by opening a new terminal and running the client.py file in it. The output of the above code should be:

```python
User: jef
```

Now the goal of this exercise is to deserialize a json file from our client to a Python object. Then send this to our server where this will be serialized back to a json file and printed out. Lets start, First we need open and deserialize the json file:

```python
import json 
import requests

f = open('spelers.json')  
data = json.load(f)

```

Now we need to send this file to our server, we can do this with a post request (POST is used to send data to a server to create/update a resource): 

```python
import json   
import requests

f = open('spelers.json')  
data = json.load(f)

res = requests.post('http://localhost:5000/test', json = data)

if res.ok:
    print(res.json())
```

We still can't run our code, because we haven't defined the end point '/test' yet. In our server.py we can add the next code: 


```python
from flask import Flask, request, jsonify

@app.route('/test', methods=['POST'])
def test():
   return jsonify(request.json)
```

Here you can see that we use the function **jsonify**. Which will Serialize the given arguments as JSON. Now we can run the client file again and you will see the ouput in your terminal.