from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.users import BaseUsers
from controller.messages import BaseMsg

app = Flask(__name__)
#apply CORS
CORS(app)

@app.route('/')
def pichonAzul():
    return 'Pichon Azul App'


#User
@app.route('/PichonAzul/users', methods=['GET', 'POST'])
def handleUsers():
    if request.method == 'POST':
        return BaseUsers().addNewUser(request.json)
    elif request.method == 'GET':
        return BaseUsers().getAllUsers()
    else:
        return jsonify("Method Not Allowed"), 405

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

#Messages
@app.route('/PichonAzul/msg', methods=['GET'])
def handleMessages():
    if request.method == 'GET':
        return BaseMsg().getAllMessages()
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/msg/<int:mid>', methods=['GET'])
def handleMessageById(mid):
    if request.method == 'GET':
        return BaseMsg().getMessageById(mid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/post', methods=['POST'])
def postMessage():
    if request.method == 'POST':
        return BaseMsg().postMessage(request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/reply', methods=['POST'])
def replyMessage():
    if request.method == 'POST':
        return BaseMsg().replyMessage(request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/share', methods=['POST'])
def shareMessage():
    if request.method == 'POST':
        return BaseMsg().shareMessage(request.json)
    else:
        return jsonify("Method Not Allowed"), 405

if __name__ == '__main__':
    app.run()
    