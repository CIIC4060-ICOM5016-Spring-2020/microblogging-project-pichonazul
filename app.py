from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.users import BaseUsers

app = Flask(__name__)
#apply CORS
CORS(app)

@app.route('/')
def pichonAzul():
    return 'Pichon Azul App'

# This route make two things
# 1. List of all users in the systems - GET
# 2. Add a new user to the system - POST
@app.route('/PichonAzul/users', methods=['GET', 'POST'])
def handleUsers():
    if request.method == 'POST':
        return BaseUsers().addNewUser(request.json)
    else:
        return BaseUsers().getAllUsers()

@app.route('/PichonAzul/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def handleUserById(uid):
    if request.method == 'GET':
        return BaseUsers().getUserById(uid)
    elif  request.method == 'PUT':
        return BaseUsers().updateUser(uid, request.json)
    elif request.method == 'DELETE':
        return BaseUsers().deleteUser(uid)
    else:
        return jsonify("Method Not Allowed"), 405

if __name__ == '__main__':
    app.run()
    