from flask import jsonify
from model.users import UsersDAO

class BaseUsers:
    def build_map_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['username'] = row[3]
        result['password'] = row[4]
        result['email'] = row[5]
        return result

    def build_attr_dict(self, uid, first_name, last_name, username, password, email):
        result = {}
        result['uid'] = uid
        result['first_name'] = first_name
        result['last_name'] = last_name
        result['username'] = username
        result['password'] = password
        result['email'] = email
        return result

    def getAllUsers(self):
        dao = UsersDAO()
        user_list = dao.getAllUsers()
        result_list = []
        for row in user_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list)

    def getUserById(self, uid):
        dao = UsersDAO()
        user_tuple = dao.getUserById(uid)
        if not user_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(user_tuple)
            return jsonify(result), 200
    
    def addNewUser(self, json):
        first_name = json['first_name']
        last_name = json['last_name']
        username = json['username']
        password = json['password']
        email = json['email']
        dao = UsersDAO()
        uid = dao.insertUser(first_name, last_name, username, password, email)
        result = self.build_attr_dict(uid, first_name, last_name, username, password, email)
        return jsonify(result), 201

    def updateUser(self, uid, json):
        first_name = json['first_name']
        last_name = json['last_name']
        username = json['username']
        password = json['password']
        email = json['email']      
        dao = UsersDAO()
        updated_code = dao.updateUser(uid, first_name, last_name, username, password, email)
        result = self.build_attr_dict(uid, first_name, last_name, username, password, email)
        return jsonify(result), 200

    def deleteUser(self, uid):
        dao = UsersDAO()
        result = dao.deleteUser(uid)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404