from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/users/<username>')
def show_user(username):
    return f'User: {username}'

@app.route('/test', methods=['POST'])
def test():
   return jsonify(request.json)

if __name__ == '__main__':
    app.run()
