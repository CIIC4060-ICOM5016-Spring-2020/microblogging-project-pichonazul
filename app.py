from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.users import BaseUsers
from controller.messages import BaseMsg
from controller.blocks import BaseBlocks
from controller.follows import BaseFollows
from controller.likes import BaseLikes


app = Flask(__name__)
app
#apply CORS
CORS(app)

@app.route('/')
def pichonAzul():
    return 'To access the app start with /PichonAzul'

@app.route('/PichonAzul')
def pichonAzulHome():
    return 'Pichon Azul App'

#Users
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
        return BaseUsers().getUserById(uid=uid)
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

#Blocks
@app.route('/PichonAzul/block/<int:uid>', methods=['POST'])
def blockUser(uid):
    if request.method == 'POST':
        return BaseBlocks().blockUser(request.json, b_uid=uid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/blockedby/<int:uid>', methods=['GET'])
def getAllUsersBlockedById(uid):
    if request.method == 'GET':
        return BaseBlocks().getBlockedById(r_uid=uid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/blocking/<int:uid>', methods=['GET'])
def getUsersBlocking(uid):
    if request.method == 'GET':
        return BaseBlocks().getAllUsersBlockingId(b_uid=uid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/unblock/<int:uid>', methods=['POST'])
def unblockUser(uid):
    if request.method == 'POST':
        return BaseBlocks().unblockUser(request.json, b_uid=uid)
    else:
        return jsonify("Method Not Allowed"), 405

#Follows

@app.route('/PichonAzul/follow/<int:uid>', methods=['POST'])
def followUser(uid):
    if request.method == 'POST':
        return BaseFollows().followUser(request.json, f_uid=uid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/followedby/<int:uid>', methods=['GET'])
def getAllUsersFollowedById(uid):
    if request.method == 'GET':
        return BaseFollows().getFollowedById(r_uid=uid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/follows/<int:uid>', methods=['GET'])
def getUsersFollowing(uid):
    if request.method == 'GET':
        return BaseFollows().getAllUsersFollowingId(f_uid=uid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/unfollow/<int:uid>', methods=['POST'])
def unfollowUser(uid):
    if request.method == 'POST':
        return BaseFollows().unfollowUser(request.json, f_uid=uid)
    else:
        return jsonify("Method Not Allowed"), 405

#Likes

@app.route('/PichonAzul/like/<int:mid>', methods=['POST'])
def likeMessage(mid):
    if request.method == 'POST':
        return BaseLikes().likeMessage(request.json, l_mid=mid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/likedby/<int:mid>', methods=['GET'])
def getAllLikesId(mid):
    if request.method == 'GET':
        return BaseLikes().getLikedById(l_mid=mid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/likes/<int:mid>', methods=['GET'])
def getMessageLikes(mid):
    if request.method == 'GET':
        return BaseLikes().getAllLikesId(l_mid=mid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/PichonAzul/unlike/<int:mid>', methods=['POST'])
def unlikeMessage(mid):
    if request.method == 'POST':
        return BaseLikes().unlikeMessage(request.json, l_mid=mid)
    else:
        return jsonify("Method Not Allowed"), 405